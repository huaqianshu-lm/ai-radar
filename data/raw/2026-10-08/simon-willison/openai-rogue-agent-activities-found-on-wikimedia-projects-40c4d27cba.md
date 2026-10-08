---
title: "OpenAI “rogue” agent activities found on Wikimedia projects"
url: "https://simonwillison.net/2026/Oct/7/openai-rogue-agents-wikimedia/"
source_url: "https://simonwillison.net/2026/Oct/7/openai-rogue-agents-wikimedia/"
canonical_url: "https://simonwillison.net/2026/Oct/7/openai-rogue-agents-wikimedia/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-07T00:16:45+00:00"
fetched_at: "2026-10-08T02:35:04+00:00"
content_type: "markdown"
is_list_page: false
---

OpenAI “rogue” agent activities found on Wikimedia projects
Given how tempting a target wikis are for rogue agent swarms, it's not a huge surprise that Wikipedia found evidence of that activity once they went looking:
The Wikimedia Foundation conducted its own investigation to see whether Wikimedia websites had been similarly affected by AI agents, focusing on those operated by OpenAI. We can confirm that we have discovered some activity by these “rogue” OpenAI agents on Wikimedia platforms. The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic, which are described more below.
They found evidence of agents editing sandbox pages, trying to use pieces of infrastructure such as Etherpad to help proxy content from elsewhere, and saw widespread crawling and "hundreds of thousands of data queries" to their Wikidata Query Service.
My best guess is that most of this was a similar (or the same) swarm of agents as those that
defaced that German wiki
while training for research tasks.
The Wikipedia sandbox wiki edits appear to have started on May 12th, and the initial test edits to the UseModWiki Sandbox page reported by that incident started on May 11th.
Tags:
wikimedia
,
wikipedia
,
wikis
,
ai
,
generative-ai
,
llms
,
ai-ethics
,
accidental-cyberattacks
