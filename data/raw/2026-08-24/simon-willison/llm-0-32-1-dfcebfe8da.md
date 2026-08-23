---
title: "llm 0.32.1"
url: "https://simonwillison.net/2026/Aug/21/llm/"
source_url: "https://simonwillison.net/2026/Aug/21/llm/"
canonical_url: "https://simonwillison.net/2026/Aug/21/llm/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-08-21T17:16:13+00:00"
fetched_at: "2026-08-23T23:22:03+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
llm 0.32.1
Fresh installs of LLM stopped working the other day because the OpenAI Python library dropped its usage of
httpx
, and it turned out LLM depended on that library but only installed it via a transitive
openai
dependency.
This dot-release fixes that for the moment by pinning to
openai<3
, and a soon-to-drop 0.33 release will switch from
httpx
to
httpx2
.
Tags:
httpx
,
openai
,
llm
