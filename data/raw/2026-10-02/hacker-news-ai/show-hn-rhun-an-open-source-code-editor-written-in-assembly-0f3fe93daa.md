---
title: "Show HN: Rhun, an open-source code editor written in assembly"
url: "https://rhun.app/"
source_url: "https://news.ycombinator.com/item?id=49926726"
canonical_url: "https://rhun.app/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-01T20:32:18+00:00"
fetched_at: "2026-10-02T02:02:36+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49926726
Original URL: https://rhun.app/
Author: vladcodes
Score: 35

I found that I'm not using even 1/3 of vim/vscode features anymore.
That's wht I'm building rhun - a small code editor for Linux, Windows and Apple silicon Macs. It obviously has Vim mode, a terminal, Git diffs and a panel for Claude Code or Codex sessions.
The editor and pixel renderer share an x86-64 assembly core. For Apple silicon, a build-time translator converts that core to AArch64, with separate platform adapters around it.
The latest release can draft commit messages using a local Ollama model or an existing Claude Code or Codex subscription.
It's a solo project, MIT licensed and still early.
