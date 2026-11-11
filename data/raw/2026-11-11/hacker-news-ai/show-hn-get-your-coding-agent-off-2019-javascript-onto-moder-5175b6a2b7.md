---
title: "Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives"
url: "https://github.com/GoogleChrome/modern-web-guidance"
source_url: "https://news.ycombinator.com/item?id=50443812"
canonical_url: "https://github.com/GoogleChrome/modern-web-guidance"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-10T18:01:15+00:00"
fetched_at: "2026-11-11T02:34:10+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50443812
Original URL: https://github.com/GoogleChrome/modern-web-guidance
Author: paulirish
Score: 273

Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without <span>s everywhere, `<dialog>` and showModal() give you backdrops and ideal focus management, `field-sizing` to auto-grow textareas as the user types.. (Something yesterday's ftrain post touched on [0])
Models know about some of these by name, but consistently won't default to using the platform-native solution and instead prefer the incumbent <div>+JS based pattern.  We started an effort in Chrome to supplement coding agents with this key domain knowledge and we're shipping our 1.0 today, in collaboration with Firefox, MDN, and Edge.
200+ guides (~1.7MB) of curated, hand-crafted implementation best-practices from web experts, updated as the web evolves.  (Open source, obv, so.. we'll welcome your bikeshedding ;) Readable versions here: [1]
I've spent the last 9 months obsessing over how to ship this as an agent skill + (Agentic RAG) CLI without blowing up your context window. (Or cedeing activation mechanics to MCP dynamic tool search). The skill description is minmaxed for activating on relevant frontend tasks. The RAG work I'm pretty proud of… originally a 500mb native stack down to a ~7MB pure-JS package, ~10ms search on your CPU.
We just introduced a deterministic 'legacy-scan' (trained on 30k github repos) to identify old 'n dusted patterns that your agent can modernize. (92% avg precision on held-out repos.)
People make a lot of claims about what coding agents are good/bad at. We wanted receipts, so we invested heavily in eval infra [2] to help us hill-climb, but also to identify when knowledge is common enough we can prune our guides. (Ofc, some of the things we thought AI didn't know turned out to be wrong :)  We run codex/claude/agy against 200 tasks without the skill and then with.. In total ~1,700 playwright/AST-based assertions. Agents go from 55% pass unguided to 92% guided.
Try it out:
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest install
    DISABLE_TELEMETRY=1 npx modern-web-guidance@latest search "animate dialog modal"
    DISABLE_TELEMETRY=1 npx modern-web-guidance@latest legacy-scan ./src
If you spot something wrong or weird, give us a holler!
Longer write-up on the 1.0:
https://developer.chrome.com/blog/modern-web-guidance-v1
---
0:
https://news.ycombinator.com/item?id=50416456
1:
https://developer.chrome.com/docs/modern-web-guidance/guides
2:
https://googlechrome.github.io/modern-web-guidance-src/
