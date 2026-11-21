---
title: "Show HN: OpenComputer – an open source alternative to Devin"
url: "https://github.com/diggerhq/opencomputer"
source_url: "https://news.ycombinator.com/item?id=50581403"
canonical_url: "https://github.com/diggerhq/opencomputer"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-20T20:19:56+00:00"
fetched_at: "2026-11-21T03:49:15+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50581403
Original URL: https://github.com/diggerhq/opencomputer
Author: iacguy
Score: 74

Hi HN!
Utpal here, I'm one of the founders of OpenComputer.
OpenComputer is an open source cloud coding agent for teams that can run in your own cloud account (AWS, GCP, Azure).
We run the agent harness and the sandbox on the same durable VM (architecture in the docs [1]). First commit lands in 24s; the alternatives we benchmarked took 53-72s (benchmarks below [2]).
Two other choices:
- One VM per team, scalable horizontally. Sessions are isolated in git worktrees.
- Session files are backed up to a repo after every turn, so any session can resume on another VM.
We noticed that past ~640 session-hours a month, one always-on 4 vCPU VM is cheaper than per-session E2B sandboxes, for example. So at scale, this setup would not only be faster than current SOTA coding agents, but also more cost-efficient.
Feel free to try via cloud for free [4] or self host. We would love any and all feedback, and happy to answer any questions! Full demo below [3].
[1]:
https://docs.opencomputer.dev/getting-started/architecture
[2]:
https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/
[3]:
https://x.com/IgorZIJ/status/2121309785882591711
[4]:
https://app.opencomputer.dev
