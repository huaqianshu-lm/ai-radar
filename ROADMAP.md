# AI Radar Roadmap

更新时间：2026-07-06

## 当前阶段

v0 本地 AI 情报雷达已经进入日常流程完善阶段。

当前主线是稳定这条链路：

```text
固定来源配置 → 抓取 raw → 生成 items JSONL → 生成 brief input → 可选生成内部简报 → 可选生成公众号 Markdown 草稿 → 可选本机定时运行
```

## 已完成

- 已建立 v0 项目边界：只做本地固定来源抓取、raw 保存、items 归一化、brief input、Claude Code CLI 简报生成和公众号 Markdown 草稿生成。
- 已建立核心目录约定：`config/`、`data/raw/`、`data/items/`、`data/inbox/`、`data/briefs/`、`data/wechat/drafts/`、`data/tracking/`、`scripts/`、`logs/`。
- 已实现公开 RSS / 普通网页来源抓取，并把原始资料保存为 Markdown + frontmatter。
- 已实现 items JSONL 生成，字段结构已固定。
- 已确认 items 去重策略：raw 每日保留快照，items 默认过滤最近 14 天历史重复内容。
- 已实现 brief input 生成。
- 已实现通过 Claude Code CLI 可选生成内部 Markdown 简报。
- 已实现简报质量检查，覆盖必要章节、禁用内容、Top 5 结构、次级关注结构、摘要长度、GitHub Trending 数量和来源链接。
- 已确认简报结构：今日最重要的 5 件事、次级关注 5 条、GitHub Trending 技术趋势观察。
- 已确认公众号草稿默认采用“个人观察型”风格，而不是日报、研报或项目复盘风格。
- 已在项目规则中明确：AI Radar 不做前端、后端、数据库、向量库、RAG、Claude API 自动化、登录态抓取、部署、自动发布公众号文章或调用 `wechat-writer`。

## 进行中

- 公众号 Markdown 草稿生成链路已经加入项目范围，当前工作区存在相关未提交实现：`scripts/generate_wechat_draft.py`、`config/wechat_draft_prompt.md`、`data/wechat/`、`scripts/run_daily.py` 和 `ai-radar` 入口更新。
- macOS 用户级 `launchd` 本机定时运行已经加入项目范围，当前工作区存在相关未提交实现：`scripts/install_launchd.py`、README 和 CLAUDE 说明更新。
- 核心 AI 公司来源覆盖规则正在强化：Anthropic、OpenAI、Google DeepMind、Meta AI、Mistral AI 等来源当天存在时，简报必须覆盖到 Top 5、次级关注或其他值得关注中。
- 低优先级聚合来源正在扩充：The Rundown AI、Reddit、TLDR Tech、Product Hunt 作为官方/开发者来源不足时的兜底信号。

## 待验证

- 需要验证生成内部简报：`.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief`。
- 需要验证生成公众号 Markdown 草稿：`.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief --generate-wechat-draft --overwrite-wechat-draft`。
- 需要验证独立公众号草稿命令：`.venv/bin/python scripts/generate_wechat_draft.py --date YYYY-MM-DD --overwrite`。
- 需要验证 `launchd` 安装、状态查看和卸载命令：`.venv/bin/python scripts/install_launchd.py install`、`status`、`uninstall`。

## 待办

- 连续观察日常运行质量，重点看 raw 内容质量、核心 AI 公司来源是否被覆盖、GitHub Trending 是否真实有参考价值。
- 根据实际简报结果继续调整 `config/brief_prompt.md`，避免聚合来源挤掉官方来源。
- 根据公众号草稿实际输出，继续收敛 `config/wechat_draft_prompt.md` 的风格和信息取舍规则。
- 确认 `launchd` 定时运行在本机 8:00 能稳定完成全流程，并检查 `logs/launchd.out.log`、`logs/launchd.err.log`。

## 阻塞

- 暂无代码层面阻塞。
- 公众号草稿和 `launchd` 链路尚未在本记录中确认已完成验证，因此不能标记为已完成。

## 最近验证

- 2026-07-06 已运行：`.venv/bin/python scripts/run_daily.py`。
- 验证结果：基础流程完成，新增 raw 文件 3 个，生成 `data/items/2026-07-06.jsonl`、`data/inbox/2026-07-06-brief-input.md`、`data/inbox/2026-07-06-run-summary.md`。
- 运行提醒：The Rundown AI 和 Reddit 抓取失败，已由流程记录为失败来源；Product Hunt 摘要偏短，生成简报时需要注意信息不足。
