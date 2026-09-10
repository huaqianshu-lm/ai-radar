---
title: "Show HN: Self-hosted company OS, Claude Code and Codex agents in departments"
url: "https://github.com/OtoDock/oto-dock"
source_url: "https://news.ycombinator.com/item?id=49630606"
canonical_url: "https://github.com/OtoDock/oto-dock"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-09T17:57:55+00:00"
fetched_at: "2026-09-10T00:53:36+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49630606
Original URL: https://github.com/OtoDock/oto-dock
Author: dimitrismrtzs
Score: 38

Hi HN, I am Dimitris. 
This is a company OS that I built and use to run my business and anyone can install it and self host it for free. Think of it as Claude Code, Cowork and the cloud sessions in one self hosted application.
It is a Multi-tenant application by design where many people can collaborate on the company agents with 4 different modes of collaboration, and it runs with your Anthropic or OpenAi subscription or even with local models.
Every agent can run on Claude Code or Codex CLI running as a persistent process on your server in a kernel sandbox (bubblewrap) with network isolation always on (pasta), with its own workspace, memory, schedules and tools. The same agents can also be configured to run identical on any remote computer through one outbound WebSocket (no inbound ports, no VPN needed).
The agent already have lots of built in features, as an example they can answer and place phone calls through Twilio or your own Asterisk, they can edit videos and excel, word, ppt files and preview them directly inside the chat with collabora and many more.
Trying it is one install script and a docker compose, no signup. The license is Fair Source, all the code is public and self hosting is free up to 5 users. 1.6.0 went out today.
AI Disclaimer: large parts of OtoDock are written using OtoDock itself, running Claude Code.
I would love people to read the code, take a look in the sandbox model, and tell me what would stop you from running this on your own hardware.
GitHub:
https://github.com/OtoDock/oto-dock
Website:
https://otodock.io
