# AI Radar

个人 AI 情报雷达 v0。

当前版本只实现：固定来源配置、抓取 raw、生成 items JSONL、生成 brief input，并可选调用 Claude Code CLI 生成 Markdown 简报。不接 Claude API。

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

推荐一条命令跑完整流程，并自动生成简报：

```bash
./ai-radar
```

等价于：

```bash
.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief
```

这会依次完成：

1. 抓取固定来源到 `data/raw/`
2. 生成当天 `data/items/YYYY-MM-DD.jsonl`
3. 生成 `data/inbox/YYYY-MM-DD-brief-input.md`
4. 调用 Claude Code CLI 生成 `data/briefs/YYYY-MM-DD-ai-daily-brief.md`

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

## v0 不做

- 前端
- 后端
- 数据库
- 向量库
- 部署
- Claude API 自动生成
- X / 微信公众号 / YouTube 抓取
