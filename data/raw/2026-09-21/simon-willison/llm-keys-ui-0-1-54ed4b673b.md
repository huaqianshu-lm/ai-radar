---
title: "llm-keys-ui 0.1"
url: "https://simonwillison.net/2026/Sep/20/llm-keys-ui/"
source_url: "https://simonwillison.net/2026/Sep/20/llm-keys-ui/"
canonical_url: "https://simonwillison.net/2026/Sep/20/llm-keys-ui/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-09-20T19:22:19+00:00"
fetched_at: "2026-09-21T00:54:20+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
llm-keys-ui 0.1
This plugin solves a very specific problem.
I've started using
Codex Remote
to run coding agents on various machines while controlling them from my phone.
Sometimes I use those machines to hack on LLM projects, and occasionally that means I need to configure an API key.
I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly.
With this plugin, I can tell Codex to run:
uvx --with llm-keys-ui llm keys-ui --all
Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys.
Then later it can use a command like
llm keys get anthropic
as part of a shell command when it needs to use a key.
Tags:
llm
,
coding-agents
,
codex
