---
title: "Show HN: I built a post-mortem debugger for native Windows x64/x86 crashes"
url: "https://www.forensicdbg.com"
source_url: "https://news.ycombinator.com/item?id=49821086"
canonical_url: "https://www.forensicdbg.com"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-23T19:15:55+00:00"
fetched_at: "2026-09-24T01:10:55+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49821086
Original URL: https://www.forensicdbg.com
Author: Loren_SL
Score: 26

Hello HN!
I've spent years debugging Windows crashes with tools that were either friendly but limited (e.g. Visual Studio) or powerful but archaic (e.g. WinDbg). I developed patterns and methods for understanding what was going on, and decided to build it into a much more effective debugging tool called ForensicDbg.
I built a modern interface to minimize the friction when debugging. All of the data shown to you is analyzed, interpreted, and presented to you clearly, so you can focus on what matters. Everything is interlinked so you can quickly and intuitivly navigate through the process space.
ForensicDbg comes with an MCP server which allows for agenic debugging. The work done to interpret and interlink your data also benefits AI tools. It removes the risk of hallucinations while building a stable foundation for them to work from without spending tokens.
If you want to try it out you can sign up and get a free beta license here:
https://www.forensicdbg.com/beta
