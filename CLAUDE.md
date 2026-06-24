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
- 原始资料保存：`data/raw/`
- 结构化条目生成：`data/items/`
- 半自动简报 Prompt：`config/brief_prompt.md`
- 简报输入文件生成：`data/inbox/YYYY-MM-DD-brief-input.md`
- 可选调用 Claude Code CLI 生成简报：`data/briefs/YYYY-MM-DD-ai-daily-brief.md`
- 本地手动命令运行
- 暂时不在简报中判断“是否值得入库”和“是否值得写文章”

v0 不做：

- 前端
- 后端服务
- 数据库
- 向量库
- RAG 框架
- Claude API 自动生成
- 登录态抓取
- X / 微信公众号 / YouTube 抓取
- 部署
- 定时任务
- 自动同步知识库

## 目录约定

```text
config/              配置和 Prompt
data/raw/            抓取到的原始资料，按日期和来源分层保存
data/items/          结构化新闻条目，JSONL 格式
data/briefs/         人工或半自动生成的 Markdown 简报
data/tracking/       趋势追踪记录，v0 不自动更新
data/inbox/          需要人工确认的内容，v0 可手动使用
scripts/             本地脚本
logs/                运行日志
```

不要新增 `src/`、Web 框架目录、数据库目录或部署目录，除非项目范围先更新。

## 数据格式约定

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
- `source`
- `source_type`
- `published_at`
- `fetched_at`
- `summary`
- `category`
- `importance_score`
- `relevance_score`
- `credibility_score`
- `should_archive`
- `should_write`
- `reason`
- `raw_path`
- `is_list_page`

v0 不做 AI 评分，`importance_score` 和 `relevance_score` 默认为 `0`，等待人工或 Claude Code 简报阶段判断。

`is_list_page: true` 表示该条目来自来源列表页，只作为兜底候选，生成简报时优先级低于单篇文章。

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

推荐完整流程，并自动调用 Claude Code CLI 生成 brief：

```bash
./ai-radar
```

等价于：

```bash
.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief
```

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

## 工程纪律

- 优先保持脚本简单，不为 v0 做复杂抽象
- 不引入数据库、队列、服务端框架、前端框架
- 不添加未要求的自动化能力
- 不抓取需要登录、强反爬或版权风险高的来源
- 外部来源失败时记录失败，不让整个流程崩掉
- 不把 API key、token、账号信息写入项目
