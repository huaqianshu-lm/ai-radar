# AI Radar

个人 AI 情报雷达 v0。

当前版本只实现：固定来源配置、抓取 raw、生成 items JSONL、生成 brief input，并可选调用 Claude Code CLI 生成 Markdown 简报、导出到本地配置的独立 Obsidian Vault。不接 Claude API。X 只支持通过本地 `X_BEARER_TOKEN` 读取显式配置的 API 来源，不做登录态抓取或泛化网页抓取。

## 安装

推荐使用 `uv`：

```bash
uv sync
```

或使用 Python 原生环境：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 使用

推荐一条命令跑完整流程，自动生成简报，并同步到配置好的 Obsidian Vault：

```bash
./ai-radar
```

等价于：

```bash
.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief --export-obsidian --overwrite-obsidian
```

这会依次完成：

1. 抓取固定来源到 `data/raw/`
2. 生成当天 `data/items/YYYY-MM-DD.jsonl`
3. 生成 `data/inbox/YYYY-MM-DD-brief-input.md`
4. 调用 Claude Code CLI 生成 `data/briefs/YYYY-MM-DD-ai-daily-brief.md`
5. 简报质量检查通过后，复制到配置好的 Obsidian Vault

如果只想抓取和准备输入，不生成简报：

```bash
.venv/bin/python scripts/run_daily.py
```

也可以分步运行：

```bash
.venv/bin/python scripts/fetch_sources.py
.venv/bin/python scripts/normalize_items.py
.venv/bin/python scripts/prepare_brief_input.py
.venv/bin/python scripts/generate_brief.py
```

如果当天简报已存在，需要重新生成：

```bash
.venv/bin/python scripts/generate_brief.py --overwrite
```

## 同步到独立 Obsidian Vault

如果希望在手机端 Obsidian 查看每日新闻，建议为 AI Radar 单独创建一个 Vault，例如 `AI Radar`，不要混入已有知识库 Vault。

在本地 `.env.local` 中配置 Vault 路径：

```bash
OBSIDIAN_VAULT_PATH="/path/to/AI Radar"
```

默认会导出到独立 Vault 内的 `Daily Briefs/` 目录：

```bash
.venv/bin/python scripts/export_obsidian.py --date YYYY-MM-DD
```

如果目标文件已存在，默认不会覆盖；需要覆盖时加：

```bash
.venv/bin/python scripts/export_obsidian.py --date YYYY-MM-DD --overwrite
```

如果想自定义 Vault 内目录，可以额外配置：

```bash
OBSIDIAN_AI_RADAR_DIR="Daily Briefs"
```

## 当前规则

- raw 每天保留抓取快照，不因为重复而删除。
- items 生成时会过滤最近 14 天历史重复内容，避免 brief input 反复出现旧内容。
- 每次运行会生成 `data/inbox/YYYY-MM-DD-run-summary.md`，记录输出文件、去重状态、来源状态、简报质量检查结果和 Obsidian 导出状态。
- 自动生成简报时，`scripts/check_brief.py` 会检查必要章节、禁用内容、Top 5 结构、次级关注结构、摘要长度、GitHub Trending 数量和来源链接。
- 简报 Top 5 优先选择单篇文章，不优先选择列表页；来源不足时不硬凑，要明确写“今日候选不足”。
- Top 5 默认单一来源最多 2 条；如果超过 2 条，必须在「今日判断」中解释该来源为什么构成当天核心信号。
- Top 5 摘要应以 150–300 字为主，最多不超过 500 字；候选材料信息不足时必须明确说明缺少哪些细节。
- 简报额外保留「次级关注 5 条」，用于放值得继续看、但不够进入 Top 5 的内容；候选不足时可以少于 5 条，但必须明确说明。

## 公众号草稿风格

当把 AI Daily Brief 整理成公众号草稿时，默认使用“个人观察型”风格：用一个核心判断统领全文，不原样搬运内部简报，不写成日报、研报或项目复盘；保留原始来源链接，方便发布前人工核查。

## v0 不做

- 前端
- 后端
- 数据库
- 向量库
- RAG 框架
- 部署
- 定时任务
- Claude API 自动生成
- 登录态抓取
- 泛化 X 抓取、X 网页抓取或动态账号发现
- 微信公众号 / YouTube 抓取
