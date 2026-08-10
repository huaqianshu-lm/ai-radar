# AI Radar 项目规则

## 项目定位

AI Radar 是一个个人使用的 AI 情报雷达本地工程。

v0 目标只有一个：

```text
固定来源配置 → 抓取 raw 原始资料 → 生成 items JSONL → 生成 brief input → 可选调用 Claude Code CLI 生成简报
```

## 当前范围

v0 只做：

- 固定来源配置：`config/sources.yaml`
- 公开 RSS / 普通网页抓取
- 通过本地环境变量、被 git 忽略的 `.env.local` 或 GitHub Actions Secrets 中的 `X_BEARER_TOKEN`，读取显式配置的 X API 来源
- 通过本地环境变量、被 git 忽略的 `.env.local` 或 GitHub Actions Secrets 中的 `PRODUCT_HUNT_TOKEN`，读取显式配置的 Product Hunt 公开产品数据
- 原始资料保存：`data/raw/`
- 结构化条目生成：`data/items/`
- 半自动简报 Prompt：`config/brief_prompt.md`
- 简报输入文件生成：`data/inbox/YYYY-MM-DD-brief-input.md`
- 可选调用 Claude Code CLI 生成简报：`data/briefs/YYYY-MM-DD-ai-daily-brief.md`
- 可选导出每日简报到本地配置的独立 Obsidian Vault
- 本地手动命令运行
- GitHub Actions 远程抓取：定时或手动只抓取 raw，并发布到独立 `remote-news` 分支；本地同步后继续运行 items、brief、Claude Code CLI、Obsidian 和 Memora
- 简报输出经过 AI 判断的 Memora 入库候选；只有“直接入库”且能找到完整 raw 原文的候选自动生成 Memora note，“先观察”和来源信息不足的内容不写入
- 暂时不在简报中判断“是否值得写文章”

v0 不做：

- 前端
- 后端服务
- 数据库
- 向量库
- RAG 框架
- Claude API 自动生成
- 登录态抓取
- 泛化 X 抓取、X 网页抓取或动态账号发现
- 微信公众号 / YouTube 抓取
- 前端 / 后端部署
- GitHub Actions 中运行 Claude Code CLI、Obsidian 或 Memora
- 自动更新已有知识卡片、主题追踪或建立双向链接
- 将 AI Radar 候选直接写入独立 Obsidian Vault 的 `Knowledge Cards/`

## 目录约定

```text
config/              配置和 Prompt
data/raw/            抓取到的原始资料，按日期和来源分层保存
data/items/          结构化新闻条目，JSONL 格式
data/briefs/         人工或半自动生成的 Markdown 简报
data/tracking/       趋势追踪记录，v0 不自动更新
data/inbox/          brief input、运行摘要和自动入库过程产物
scripts/             本地脚本
logs/                运行日志
```

不要新增 `src/`、Web 框架目录、数据库目录或部署目录，除非项目范围先更新。

## 数据格式约定

### X API 来源约束

- 只允许读取 `config/sources.yaml` 中显式配置的 X API 来源
- 只使用 `X_BEARER_TOKEN`，来源为本地环境变量、被 git 忽略的 `.env.local` 或 GitHub Actions Secrets
- 不做登录态网页抓取、Cookie 抓取、动态账号发现或批量扫号
- token 不得写入日志、raw、items、brief input、brief 或 run summary

### Product Hunt API 来源约束

- 只允许读取 `config/sources.yaml` 中显式配置的 Product Hunt 来源
- 只使用 `PRODUCT_HUNT_TOKEN`，来源为本地环境变量、被 git 忽略的 `.env.local` 或 GitHub Actions Secrets
- 只读取公开产品数据，不进行任何写操作或用户数据读取
- token 不得写入日志、raw、items、brief input、brief 或 run summary

### raw

raw 使用 Markdown + frontmatter：

```markdown
---
title: Example
url: https://example.com
source: Example Source
source_type: official
published_at: 2026-06-21T00:00:00
fetched_at: 2026-06-21T09:00:00
content_type: markdown
---

正文或摘要。
```

raw 原则：

- 只追加，不覆盖已有文件
- 必须保留原始链接
- 正文抓不到时，至少保留标题、链接、摘要和来源

### items

items 使用 JSONL：

```text
data/items/YYYY-MM-DD.jsonl
```

每行一个 JSON 对象，字段固定：

- `title`
- `url`
- `source_url`
- `canonical_url`
- `source`
- `source_type`
- `published_at`
- `fetched_at`
- `summary`
- `display_summary`
- `category`
- `importance_score`
- `relevance_score`
- `credibility_score`
- `should_archive`
- `should_write`
- `reason`
- `raw_path`
- `is_list_page`
- `cluster_key`
- `cluster_basis`
- `cluster_size`
- `cluster_rank`

`summary` 是供 brief 判断使用的较完整候选摘要；`display_summary` 是供未来前端卡片展示的短摘要，由 raw 正文确定性截断生成，brief 仍优先使用 `summary`。

v0 不做 AI 评分，`importance_score` 和 `relevance_score` 默认为 `0`，等待人工或 Claude Code 简报阶段判断。

`is_list_page: true` 表示该条目来自来源列表页，只作为兜底候选，生成简报时优先级低于单篇文章。

### items 去重

三天验证后确认采用：每天继续抓取所有来源，但生成 items 时过滤最近 14 天历史重复内容。

去重原则：

- raw 保留每日抓取快照，不因为重复而删除
- items 默认只保留进入当日 brief input 的新增内容
- URL 去重前需要做规范化，至少去掉 fragment、常见 tracking 参数和末尾 `/`
- 标题规范化后相同，视为重复候选
- GitHub Trending 中同一 repo URL 重复时不再进入当天 items
- run summary 应记录扫描 raw 数、写入 items 数、当日重复过滤数、历史重复过滤数

## 简报生成规则

三天验证后确认当前 brief 结构继续沿用：

- 每日简报保留「今日最重要的 5 件事」
- 额外保留「次级关注 5 条」
- 额外保留「GitHub Trending 技术趋势观察」
- Top 5 优先选择单篇文章，不优先选择列表页
- Top 5 默认单一来源最多 2 条；如果超过 2 条，必须在「今日判断」中解释该来源为什么构成当天核心信号
- 来源不足时不要硬凑 Top 5，要明确说明候选不足
- 只有“直接入库”且 raw 原文完整可追溯的候选会自动进入 Memora；“先观察”和来源信息不足的内容只保留在简报中
- Memora note 完成后必须更新 `knowledge/index.md`、`knowledge/log.md`，并在 `knowledge/知识库总览.md` 添加原文链接和 note 链接
- 暂时不判断“是否值得写文章”

Top 5 的摘要规则：

- 每条 Top 5 使用 2–4 个项目符号概括事实，要点合计以 100–250 字为宜；候选材料信息不足时可以更短
- 要点必须共同说明：对象、发生了什么变化、核心信息、可能用途或趋势意义
- 每条必须有非空的发布时间、影响判断和原文链接；影响段落同时说明为什么重要，以及对我的 AI 编程、产品判断、AI 工具链或长期趋势观察的影响
- 如果候选材料没有提供能力、参数、发布时间、性能指标等细节，必须明确写“候选材料未提供……”
- 不要只复述 raw summary 的一句话，也不要把同一事实拆成多个重复区块
- 不要编造候选材料没有提供的信息

次级关注规则：

- 优先输出 5 条，候选不足时可以少于 5 条，但必须明确说明“今日候选不足”
- 每条用 2–3 句话说明这是什么、为什么暂时值得放着、后续看什么
- 不要和 Top 5 重复
- 不需要展开成完整 Top 5 格式

## 公众号草稿风格

当把 AI Daily Brief 整理成公众号草稿时，默认使用 2026-06-25 验证通过的“个人观察型”风格：

- 不要原样搬运内部简报，不要写成日报、研报或项目复盘
- 用一个核心判断统领全文，而不是平均罗列所有条目
- 标题要像人的观察，例如“今天看到一个信号：AI 公司开始卷‘模型之外’的东西了”
- 开头从“我看到什么信息后停下来”切入，少用宏大背景铺垫
- 正文允许保留一人称判断，如“我现在不会把它当成确定结论”“我更关心……”
- 句子要有自然停顿，减少模板句，避免反复使用“这说明”“值得关注”“对我的影响”
- 信息取舍优先于完整罗列，必要时把多个条目合并成 2–4 个核心信号
- 每个信号都解释：它是什么、为什么现在值得看、对 AI 产品/工具/个人工作流有什么启发
- 对不确定信息明确写“不确定”“先观察”“缺少关键细节”，不要为了显得完整而编造
- 结尾给出一句可传播的个人判断，但不要鸡汤化
- 保留原始来源链接，方便发布前人工核查

## 运行命令

安装依赖：

```bash
uv sync
```

如果不用 `uv`：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

推荐完整流程，不自动生成 brief：

```bash
.venv/bin/python scripts/run_daily.py
```

推荐完整流程，并自动调用 Claude Code CLI 生成 brief，再同步到配置好的 Obsidian Vault：

```bash
./ai-radar
```

等价于：

```bash
.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief --export-obsidian --overwrite-obsidian
```

远程抓取后的本地同步与完整处理：

```bash
./ai-radar --remote
```

该命令只同步远程 raw，不在本地重复抓取来源；后续处理仍由本地 AI Radar、Claude Code CLI、Obsidian 和 Memora 完成。

分步抓取 raw：

```bash
.venv/bin/python scripts/fetch_sources.py
```

分步生成 items：

```bash
.venv/bin/python scripts/normalize_items.py
```

分步生成 brief input：

```bash
.venv/bin/python scripts/prepare_brief_input.py
```

分步调用 Claude Code CLI 生成 brief：

```bash
.venv/bin/python scripts/generate_brief.py
```

指定日期生成 items、brief input 或 brief：

```bash
.venv/bin/python scripts/normalize_items.py --date YYYY-MM-DD
.venv/bin/python scripts/prepare_brief_input.py --date YYYY-MM-DD
.venv/bin/python scripts/generate_brief.py --date YYYY-MM-DD
```

只处理已经存在的 raw：

```bash
.venv/bin/python scripts/run_daily.py --skip-fetch --date YYYY-MM-DD
```

## 验证方式

每次改动脚本后至少运行：

```bash
.venv/bin/python scripts/run_daily.py
```

成功标准：

- `data/raw/YYYY-MM-DD/` 下生成 Markdown raw 文件，或脚本明确报告来源抓取失败原因
- `data/items/YYYY-MM-DD.jsonl` 生成成功
- `data/inbox/YYYY-MM-DD-brief-input.md` 生成成功
- 如使用 `--generate-brief`，`data/briefs/YYYY-MM-DD-ai-daily-brief.md` 生成成功
- 如使用 `--export-obsidian`，简报质量检查通过后同步到配置好的 Obsidian Vault；若导出失败，应在 run summary 中记录原因

## 工程纪律

- 优先保持脚本简单，不为 v0 做复杂抽象
- 不引入数据库、队列、服务端框架、前端框架
- 不添加未要求的自动化能力
- 不抓取需要登录、强反爬或版权风险高的来源
- 外部来源失败时记录失败，不让整个流程崩掉
- 不把 API key、token、账号信息写入项目
- 每次完成文件改动后，提醒用户检查并提交未提交文件
