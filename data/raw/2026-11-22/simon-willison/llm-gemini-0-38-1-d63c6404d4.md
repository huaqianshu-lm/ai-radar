---
title: "llm-gemini 0.38.1"
url: "https://simonwillison.net/2026/Nov/20/llm-gemini/"
source_url: "https://simonwillison.net/2026/Nov/20/llm-gemini/"
canonical_url: "https://simonwillison.net/2026/Nov/20/llm-gemini/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-20T03:01:57+00:00"
fetched_at: "2026-11-22T02:51:43+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
llm-gemini 0.38.1
Gemini 4 Carbon only supports
low
,
medium
and
high
reasoning levels - but Gemini 4 Hydrogen and Gemini 4 Neon both have an extra
xhigh
level.
I missed that when I added those models to the
llm-gemini
plugin, which is now fixed in this dot release.
The
xhigh
setting for Hydrogen makes a
significant
difference. I updated my
Gemini 4 comparison grid
- note how Hydrogen at high used 5,311 output tokens and cost 3.99 cents, but the same model at xhigh used 31,477 output tokens, cost 23.61 cents, and produced a pelican that's competitive with Gemini 4 Neon:
Tags:
gemini
,
llm
,
llm-reasoning
,
pelican-riding-a-bicycle
,
ai
,
llms
,
google
,
generative-ai
