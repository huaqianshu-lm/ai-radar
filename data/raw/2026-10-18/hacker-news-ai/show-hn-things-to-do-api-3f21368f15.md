---
title: "Show HN: Things to Do API"
url: "https://thingstodoapi.com/"
source_url: "https://news.ycombinator.com/item?id=50126384"
canonical_url: "https://thingstodoapi.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-16T23:58:34+00:00"
fetched_at: "2026-10-18T00:41:48+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50126384
Original URL: https://thingstodoapi.com/
Author: invalidmonk
Score: 33

I built an api/mcp for local events: pop-ups, one-off events, concerts, etc. currently covering the SF bay area.
I've been building a bunch of consumer apps lately around personalization and recommendation and have had a hard time finding this data in one spot. agents can find useful stuff through tool calls / web search, but slow.
you can scrape on demand too, but i wanted a faster data set and couldn't find an existing provider for the mix of event types I was searching for.
the methodology for it is to find influential accounts/posters/etc. and do a fan out across things that they co-post with.
mcp: `claude mcp add --transport http thingstodo
https://api.thingstodoapi.com/mcp
`
I'm considering adding other cities. If you're building something that needs local event data, would something like this be useful and where would you want coverage?
