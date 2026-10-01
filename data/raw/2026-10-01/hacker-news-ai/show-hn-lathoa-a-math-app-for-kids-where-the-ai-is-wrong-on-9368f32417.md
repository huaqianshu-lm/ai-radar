---
title: "Show HN: Lathoa, a math app for kids where the AI is wrong on purpose"
url: "https://lathoa.ai/en"
source_url: "https://news.ycombinator.com/item?id=49909648"
canonical_url: "https://lathoa.ai/en"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-30T14:38:57+00:00"
fetched_at: "2026-10-01T01:50:12+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49909648
Original URL: https://lathoa.ai/en
Author: thanouil1411
Score: 26

I made this for kids around 10 to 14. A robot called Errol solves a math problem step by step and one of the steps is wrong. The kid has to find it and say what's wrong with it. Sometimes nothing is wrong, so just saying "there's a mistake" every time doesn't work. The user needs to enter an explanation if she finds an error to gain more XP; speed matters also for more points. There is no direct interaction or chatting with an LLM. Lathoa's harness is stable and has many evaluation steps to catch inconsistencies and prompt injections.
You can play one on the homepage without signing up.
The part that surprised me: it's hard to get an LLM to be wrong on purpose. Half the time it gives you the right answer and calls it wrong, or a "mistake" that's actually correct. So every case gets checked before a kid sees it. Where it can, a plain arithmetic check redoes the math exactly. A second model also solves the problem without seeing Errol's work. If anything disagrees, the case is thrown away.
The weak spot is that the second model can make the same mistake as the first. The arithmetic check is there for that, but it only works on English cases so far. German and Greek write decimals with a comma and I haven't got the parsing right yet.
What I'd really like to know: does finding someone else's mistake teach anything that solving the problem yourself doesn't? I'm not sure, and I'd like to hear from people who teach.
