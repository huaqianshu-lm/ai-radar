# AI Radar

个人 AI 情报雷达 v0。

当前版本实现：固定来源配置、抓取 raw、生成 items JSONL、生成 brief input，并可选调用 Claude Code CLI 生成 Markdown 简报、自动判断 Memora 入库候选并生成正式 note；另提供 GitHub Actions 远程抓取工作流。不接 Claude API。重点关注视频制作、文本转音频、前端页面设计、新闻抓取、AI 产品和 AI 工具等领域。X 只支持通过显式配置的 API 来源读取数据，不做登录态抓取或泛化网页抓取。

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
6. 简报质量检查通过后，自动将“直接入库”候选写入配置的 Obsidian 知识卡片目录

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

远程抓取完成后，在本地同步 raw 并继续完整流程：

```bash
./ai-radar --remote
```

这个命令不会再次访问新闻来源，而是同步远程 raw 后在本地继续生成 items、brief、Obsidian 和 Memora 结果。

## GitHub Actions 远程抓取与本地同步

`.github/workflows/fetch-news.yml` 只负责在 GitHub Actions 中抓取 raw，不运行 items、brief、Claude Code CLI、Obsidian 或 Memora。

- 每天 `23:00 UTC`（北京时间次日 `07:00`）自动运行，也可以在 GitHub Actions 页面手动运行。
- 在仓库 `Settings → Secrets and variables → Actions` 中配置 `PRODUCT_HUNT_TOKEN`；只有重新启用 X 来源时才需要配置 `X_BEARER_TOKEN`。
- 每次成功运行会把当天 raw 发布到独立的 `remote-news` 分支；主分支和本地 `data/` 忽略规则保持不变。
- 本地 `./ai-radar --remote` 使用现有 Git 凭据同步 `remote-news` 分支，再调用本地完整处理流程。
- 运行还会生成 `ai-radar-raw-YYYY-MM-DD` Artifact 作为排查备份，默认保留 30 天；日常同步不需要手动下载 Artifact。

macOS 自动同步可以使用 [config/com.ai-radar.remote-daily.plist.example](config/com.ai-radar.remote-daily.plist.example)：

```bash
cp config/com.ai-radar.remote-daily.plist.example ~/Library/LaunchAgents/com.ai-radar.remote-daily.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ai-radar.remote-daily.plist
```

该任务每天按本地时间 08:00 和 16:00 各检查一次；电脑关机期间不会丢失远程 raw，下一次到点或开机后会继续同步和处理。


## 知识库入库

简报生成后，AI 只会把满足“直接入库”标准且能找到完整 raw 原文的候选交给 Memora 入库；“先观察”和来源信息不足的内容只保留在简报中。Memora 完成 note、索引和日志更新后，还会把原文链接与 note 链接写入 `knowledge/知识库总览.md`。

```bash
# 从当天简报自动写入“直接入库”候选；run_daily.py 生成简报时也会自动执行
.venv/bin/python scripts/archive_notes.py --date YYYY-MM-DD --apply
```

配置 `MEMORA_ROOT` 指向 Memora 项目根目录，例如 `/Users/limiao/personal/2-topic/4-AI/project/memora`。不再写入 AI Radar 独立 Vault 的 `Knowledge Cards/`。

```bash
.venv/bin/python scripts/archive_notes.py --date YYYY-MM-DD --apply
```

脚本只会写入简报中标记为“直接入库”的候选，并保留原文链接；“先观察”、来源信息不足或目标文件已存在的条目会跳过。

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
- 自动生成简报时，`scripts/check_brief.py` 会检查必要章节、禁用内容、Top 5 结构、要点与影响格式、次级关注结构、GitHub Trending 数量和来源链接。
- 简报 Top 5 优先选择单篇文章，不优先选择列表页；来源不足时不硬凑，要明确写“今日候选不足”。
- Top 5 默认单一来源最多 2 条；如果超过 2 条，必须在「今日判断」中解释该来源为什么构成当天核心信号。
- Top 5 每条使用 2–4 个要点概括事实，要点合计以 100–250 字为宜，并用一段“影响”合并说明重要性和对个人工作流的影响；候选材料信息不足时必须明确说明缺少哪些细节。
- 简报额外保留「次级关注 5 条」，用于放值得继续看、但不够进入 Top 5 的内容；候选不足时可以少于 5 条，但必须明确说明。

## 公众号草稿风格

当把 AI Daily Brief 整理成公众号草稿时，默认使用“个人观察型”风格：用一个核心判断统领全文，不原样搬运内部简报，不写成日报、研报或项目复盘；保留原始来源链接，方便发布前人工核查。

## v0 不做

- 前端
- 后端
- 数据库
- 向量库
- RAG 框架
- 前端 / 后端部署
- GitHub Actions 中运行 Claude Code CLI、Obsidian 或 Memora
- Claude API 自动生成
- 登录态抓取
- 泛化 X 抓取、X 网页抓取或动态账号发现
- 微信公众号 / YouTube 抓取
