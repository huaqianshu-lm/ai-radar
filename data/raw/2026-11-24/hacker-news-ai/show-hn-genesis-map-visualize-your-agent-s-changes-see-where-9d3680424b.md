---
title: "Show HN: Genesis Map – Visualize your agent's changes. See where they can break"
url: "https://github.com/GenesisAgentInfra/genesis"
source_url: "https://news.ycombinator.com/item?id=50623965"
canonical_url: "https://github.com/GenesisAgentInfra/genesis"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-24T05:04:41+00:00"
fetched_at: "2026-11-24T06:48:11+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50623965
Original URL: https://github.com/GenesisAgentInfra/genesis
Author: willlzl
Score: 5

When agent ships code faster and faster, human review is no longer possible. Which brings 2 problems, at least for me:
1. I need to understand what my agent changes as quickly and easily as possible, cuz I don't wanna lose track of the current status of my product, or be the main bottleneck in shipping code.
2. I don't trust what my agent tells me. Many times, I've been suffered from agent telling me "all is well", then say "you are right, sorry, I missed..." after code failed on production.
To mitigate those problems, I made Genesis, a skill for coding agent to generate a beautiful flow chart to understand all the business flows, flag all risk changes and untested code between commits. It worked very well on me, so I benchmarked it against vanilla Claude code and Codex:
Vanilla → With Genesis
1. Test gaps caught: Claude Code 8% → 38% · Codex 4% → 23%
2. False alarms per review: Claude Code 2.1 → 0.7 · Codex 1.4 → 0.5
3. Real risks found per review: Claude Code 2.9 → 2.8 · Codex 2.4 → 2.4
