# AI Radar Roadmap

## 当前阶段

v0 主链路已跑通，进入稳定性修复阶段。X API 窄口径来源接入代码暂时保留，但 X 抓取已从默认日常流程中收起，近期不再排查或运行。

已具备：固定来源配置、公开来源抓取、raw 快照、items JSONL、brief input、可选 Claude Code CLI 生成每日简报、每日简报本地导出到 Obsidian、公众号草稿生成。

暂时收起：X API recent search 固定来源接入，代码保留但默认禁用，近期不再纳入日常抓取、问题排查或提醒。

## 最近有效进度

- 2026-07-28：按版本管理策略排除公众号草稿、`settings.json` 和 `.DS_Store`，仅保留可提交项目改动；项目规则增加每次文件改动后提醒检查并提交未提交文件。
- 2026-07-27：将 Obsidian 导出接入每日流程，新增 `--export-obsidian` / `--overwrite-obsidian` 参数；`./ai-radar` 默认在简报质量检查通过后覆盖同步到配置好的 Obsidian Vault，并在 run summary 中记录导出状态。
- 2026-07-27：按用户要求暂时收起 X 抓取；`X AI Watchlist` 在 `config/sources.yaml` 中改为默认禁用，X recent search 代码保留但近期不再纳入日常抓取、问题排查或提醒。
- 2026-07-27：调整 AI Daily Brief 默认排版规范，后续生成简报改用 `example.md` 验证过的引用块、加粗小标题和分段留白格式；同步更新 2026-07-27 简报排版，并让质量检查脚本兼容新格式。
- 2026-07-27：新增最小 Obsidian 导出脚本，可将指定日期 AI Daily Brief 复制到环境变量配置的独立 Obsidian Vault；默认导出到 Vault 内 `Daily Briefs/`，已在 iCloud Obsidian 目录创建 `AI Radar` 独立 Vault 并完成 2026-07-21、2026-07-27 简报导出验证。
- 2026-07-22：新增 X API recent search 固定来源接入，支持从环境变量或 `.env.local` 读取 `X_BEARER_TOKEN`；完整流程验证通过，X 来源失败不会中断 raw/items/brief input/run summary 生成。
- 2026-07-21：完整流程恢复，生成 40 个 raw、29 条 items、brief input 和 AI Daily Brief，简报质量检查通过。
- 2026-07-13：抓取与 items 仍有部分有效产出，写入 8 条 items，但 brief 生成失败。
- 2026-07-12：已生成 AI Daily Brief 和公众号草稿，是最近一次确认有公众号草稿的日期。

## 当前问题

- Hugging Face Blog 摘要偏短，生成简报时需要注意信息不足。
- `data/wechat/` 已按当前策略加入忽略，不纳入版本管理；如后续要沉淀公众号发布稿，需要重新确认存放和提交规则。
- 公众号草稿生成没有出现在 2026-07-21 run summary 中，需要后续确认是否仍纳入自动流程。

## 下一步

1. 确认 2026-07-28 简报内容质量是否符合人工预期。
2. 确认公众号草稿是否需要继续作为每日流程的一部分。

## 最近验证

- 2026-07-28：运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/check_brief.py scripts/run_daily.py scripts/export_obsidian.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-28.jsonl`、`data/inbox/2026-07-28-brief-input.md`、`data/inbox/2026-07-28-run-summary.md`，X 来源保持禁用，公众号草稿和本地 `settings.json` 已被忽略。
- 2026-07-27：运行 `.venv/bin/python -m py_compile scripts/run_daily.py scripts/export_obsidian.py` 成功；运行 `.venv/bin/python scripts/run_daily.py --help` 成功，确认新增 `--export-obsidian` / `--overwrite-obsidian` 参数；使用临时目录作为 `OBSIDIAN_VAULT_PATH` 运行 `.venv/bin/python scripts/run_daily.py --generate-brief --export-obsidian --overwrite-obsidian` 成功导出到临时 Vault；运行 `.venv/bin/python scripts/run_daily.py --generate-brief --export-obsidian --overwrite-obsidian` 成功导出到 iCloud Obsidian `AI Radar/Daily Briefs/2026-07-27-ai-daily-brief.md`，run summary 已记录 Obsidian 导出状态。
- 2026-07-27：运行 `.venv/bin/python scripts/run_daily.py` 成功，默认流程已跳过禁用的 `X AI Watchlist`，没有再出现 X 失败日志或 X 复查提醒；生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`。
- 2026-07-27：运行 `.venv/bin/python scripts/check_brief.py --date 2026-07-27` 通过；运行 `.venv/bin/python -m py_compile scripts/check_brief.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`，X 来源因 `402` 失败且不影响主流程。
- 2026-07-27：运行 `.venv/bin/python scripts/export_obsidian.py --help` 成功；运行 `.venv/bin/python -m py_compile scripts/export_obsidian.py` 成功；使用临时目录作为 `OBSIDIAN_VAULT_PATH` 运行 `.venv/bin/python scripts/export_obsidian.py --date 2026-07-21` 成功复制到 `Daily Briefs/2026-07-21-ai-daily-brief.md`；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`，X 来源因 `402` 失败且不影响主流程；运行 `.venv/bin/python scripts/generate_brief.py --date 2026-07-27 --overwrite` 成功生成今日简报，运行 `.venv/bin/python scripts/export_obsidian.py --date 2026-07-27 --overwrite` 成功导出到 iCloud Obsidian `AI Radar/Daily Briefs/`，运行 `.venv/bin/python scripts/check_brief.py --date 2026-07-27` 通过。
- 2026-07-22：运行 `python3 -m py_compile scripts/fetch_sources.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-22.jsonl`、`data/inbox/2026-07-22-brief-input.md`、`data/inbox/2026-07-22-run-summary.md`。X 来源未取回数据，run summary 中记录为单来源失败；token 泄露扫描通过。
- 2026-07-21：运行 `.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief` 成功，`data/briefs/2026-07-21-ai-daily-brief.md` 已生成，质量检查通过。
