---
title: "llm-tools-datasette 0.1.1"
url: "https://simonwillison.net/2026/Oct/18/llm-tools-datasette/"
source_url: "https://simonwillison.net/2026/Oct/18/llm-tools-datasette/"
canonical_url: "https://simonwillison.net/2026/Oct/18/llm-tools-datasette/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-18T23:43:09+00:00"
fetched_at: "2026-10-22T01:18:40+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
llm-tools-datasette 0.1.1
When I switched LLM over to
httpx2
in
LLM 0.33
I forget that this would break any plugins which used
httpx
without directly depending on it.
llm-tools-datasette
was one of those plugins, now fixed.
Tags:
datasette
,
llm
