---
title: "llm-anthropic 0.27"
url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
source_url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
canonical_url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-08-24T16:27:04+00:00"
fetched_at: "2026-09-01T01:42:22+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
llm-anthropic 0.27
This release of the Anthropic plugin for
LLM
mainly provides compatibility with the recently released
anthropic v1.0.0
Python library, which switches from
httpx
to
httpx2
. OpenAI made the same change in their
v3.0.0 release
two weeks ago.
Anthropic provide this
migration guide
for upgrading to 1.0, so I prompted Fable 5 in Claude Code with:
Upgrade to anthropic>=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing
Here's
the resulting PR
.
Tags:
python
,
httpx
,
llm
,
anthropic
,
claude
