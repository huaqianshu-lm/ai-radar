---
title: "Quoting Prompting Claude Fable 5.2"
url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
source_url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
canonical_url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-10T05:34:14+00:00"
fetched_at: "2026-11-11T02:34:10+00:00"
content_type: "markdown"
is_list_page: false
---

Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on. In Anthropic’s testing on small coding tasks, when a prompt said nothing about ownership or presented the code base as someone else’s, the model tended to add to the existing structure, even when that repeated existing code. [...]
If you want the model to improve the structure as it works, say that the code is its own:
This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.
In Anthropic’s testing on small coding tasks, the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it.
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
