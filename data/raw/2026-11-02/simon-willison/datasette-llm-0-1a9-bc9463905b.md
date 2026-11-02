---
title: "datasette-llm 0.1a9"
url: "https://simonwillison.net/2026/Oct/31/datasette-llm/"
source_url: "https://simonwillison.net/2026/Oct/31/datasette-llm/"
canonical_url: "https://simonwillison.net/2026/Oct/31/datasette-llm/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-31T22:10:01+00:00"
fetched_at: "2026-11-02T02:09:01+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-llm 0.1a9
I have some big upgrades to
Datasette Agent
in the pipeline, but in the meantime here's a tiny user experience improvement to the underlying
datasette-llm
plugin.
It now picks up the default model used by
LLM
, which means you can start using Datasette Agent without needing to explicitly configure a default model:
uvx --with datasette-agent datasette content.db --internal internal.db
Previously you would also need to specify a model with
-s plugins.datasette-agent.default_model gpt-6-astra
.
Tags:
datasette
,
llm
,
datasette-agent
