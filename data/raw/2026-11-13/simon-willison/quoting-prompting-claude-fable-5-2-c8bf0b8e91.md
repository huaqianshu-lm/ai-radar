---
title: "Quoting Prompting Claude Fable 5.2"
url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
source_url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
canonical_url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-10T05:34:14+00:00"
fetched_at: "2026-11-13T03:13:32+00:00"
content_type: "markdown"
is_list_page: false
---

Claude Fable 5.2 pays close attention to who owns the code it works on. In Anthropic’s testing on small coding tasks, the model tended to add to the existing structure when the prompt said nothing about ownership or presented the code base as someone else’s, even when that duplicated existing code. When the prompt said the code base was the model’s own, it often consolidated duplicated code and sometimes made related fixes without being asked.
If you want the model to improve the structure as it works, say that the code is its own:
You are the owner and long-term maintainer of this codebase, and its design is up to you.
The ownership sentence makes the model much more likely to consolidate duplicated code into one shared function. In Anthropic’s testing on small coding tasks, the model consolidated duplicated code in under 10 percent of runs without the sentence and in about 75 percent of runs with it.
—
Prompting Claude Fable 5.2
, Anthropic documentation
Tags:
prompt-engineering
,
anthropic
,
generative-ai
,
ai
,
llms
,
claude-mythos-fable
