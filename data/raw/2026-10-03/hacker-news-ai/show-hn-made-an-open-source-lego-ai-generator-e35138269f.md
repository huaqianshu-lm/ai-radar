---
title: "Show HN: Made an open-source Lego AI generator"
url: "https://github.com/anteloc/ldraw-nova"
source_url: "https://news.ycombinator.com/item?id=49937916"
canonical_url: "https://github.com/anteloc/ldraw-nova"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-02T20:00:15+00:00"
fetched_at: "2026-10-03T01:46:27+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49937916
Original URL: https://github.com/anteloc/ldraw-nova
Author: antelocnova
Score: 68

Hi there :-) New on HN, first time posting.
Past year, around December, I started experimenting with making ChatGPT and Claude generate source code in LDraw language.
This LDraw is literally an "assembly" language, a low-level programming language that describes how to assemble LEGO pieces together into models, one placement instruction at a time.
When executed by specific tools, like e.g. LDView, LeoCAD, Studio... these instructions become LEGO CAD models, that can be interacted with, modified, etc.
Or, in other words: one LDraw source file in .mpd or .ldr format is equivalent to one LEGO CAD model.
So, the idea I had was: if I manage for maybe ChatGPT or Claude to generate high-quality LDraw source files... then, they would actually be generating high-quality LEGO CAD models, right?
Then, after months of iterations and trying one thing after the other... it worked!!!
Long story short: using GPT-6 Astra and Opus 5.5, I've managed to create a python toolset, instructions, and docs for agents in general. Now, these can be used by them to generate LDraw models.
I've packed it all as a dockerized web app for others to try and experiment, with several providers (and agents) to choose from: OpenAI, Claude and OpenRouter.
Here's a bunch of exmaples:
https://anteloc.github.io/index-samples.html
.
If you are curious about the internals of an .mpd model, the "what was the agent picturing on its mind", open the .mpd file that got your attention on a text editor, and read the first line under the ones starting with "0 FILE".
I'd really appreciate feedback and comments, let's see where this goes =)
