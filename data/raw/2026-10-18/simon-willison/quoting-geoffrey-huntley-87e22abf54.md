---
title: "Quoting Geoffrey Huntley"
url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley/"
source_url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley/"
canonical_url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-13T13:32:00+00:00"
fetched_at: "2026-10-18T00:41:48+00:00"
content_type: "markdown"
is_list_page: false
---

If the agent isn't using my diagnostics library, I could introspect and update AGENTS.md, but there's still a delta, and it'll drift. Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten.
—
Geoffrey Huntley
, nobody should type code by hand anymore. here's what's left.
Tags:
coding-agents
,
generative-ai
,
git
,
agentic-engineering
,
ai
,
geoffrey-huntley
,
llms
