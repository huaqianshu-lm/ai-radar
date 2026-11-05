---
title: "Launch HN: Kino AI (YC S23) – AI media manager and video editor"
url: "https://news.ycombinator.com/item?id=50368804"
source_url: "https://news.ycombinator.com/item?id=50368804"
canonical_url: "https://news.ycombinator.com/item?id=50368804"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-04T17:31:53+00:00"
fetched_at: "2026-11-05T03:15:53+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50368804
Author: lukeigel
Score: 73

Hi HN! I'm Luke from Kino (
https://kino.ai
). Kino lets you make great videos with your agents and your teammates. Storage of footage and assets, a rich video editor, and review links for teammates are all bundled into one. Your colleagues and Codex / Claude Code can work on the same timeline with review notes and footage all in one place. See a basic overview at
https://kino.ai/walkthrough-video
and our launch video (made entirely with Kino!) at
https://kino.ai/launch-video
Opus 5.5 can edit videos and make great motion graphics now. But with a raw agent harness, you need to describe tiny edits either in words or in quick one-off UIs, you can’t refer to footage shared across your devices, and feedback from teammates comes as screenshots on Slack.
Kino is code-first. All editing, all motion graphics, all dragging of timeline items around, all teammate comments, and all 3D scenes are expressed as code, built on Remotion. This was hard to get right, as we found ourselves building a what-you-see-is-what-you-get editor for React, which we then turned into a video editor. For our launch video I told Claude-with-Kino to find a macOS Leopard install disk and reskin our whole video to match.
Kino is also fully collaborative and real-time, so you can see your teammates' cursors and exactly which part of the timeline they’re currently watching. For our launch video I had 5+ agents editing the timeline concurrently while my friend Donald had his swarm working a few minutes further down. Donald had one agent rotoscoping to make our visual effects work, I had an LLM color grading all media via our LUT support, and we both made tiny tweaks to the timeline along the way.
To make this code-first editor work with video footage, everything gets transcribed, embedded, described, and face-detected. You can scrub your footage locally after you drag it in, but we upload a low-res proxy so your teammates and cloud inference can see it. This local scrubbing plus custom pro media decoders means you can drag a 250GB ProRes clip from your new iPhone right into your Kino timeline. We built custom decoders for professional codecs such as ProRes, BRAW, R3D, and more (see my extremely successful nine point HN post
https://news.ycombinator.com/item?id=50198052
). None of the performance we’re getting would have been possible before WebCodecs and libraries like Mediabunny.
I grew up making YouTube videos, and during my undergrad at MIT I co-directed a 3.5 hour archival footage documentary on the history of my school and technological development in America (
https://regressions.net
). Much of the work was logging footage, managing hard drives, manually syncing Premiere project state, and planning our movie in a spreadsheet.
Our first launch in 2023 proclaimed that Kino was "Silicon Valley meets Hollywood." It was more like Palantir for Hollywood; we ran bespoke on-prem Kino deployments with our team of forward deployed engineers on shows like Survivor and A24's Beef. It was a rush, but it felt like the slowest way to improve video editing for the whole world. Bound by the Avid Media Composer and strict studio security rules, we couldn't touch frontier models, and we couldn't make editors >10x faster. So in 2025, we rebuilt Kino as a true editor, and we took a bet on coding-as-editing.
Everything in Kino has a URL: projects, clips, footage, comments and replies, even a single frame and the line of code that draws it. Projects and media living in one place and everything being addressable means that your agents and team have a single, editable source of truth for video production. At a lower level, I now paste Kino links into my agent constantly, whether it’s making sure Codex knows exactly which timeline item (among thousands) I am referring to or which teammate’s comment needs fixing.
We have teams managing their whole company’s media in Kino, spinning up agents to make new videos every day, then using review links to flag issues. One founder ships ads like this: each day he uses Kino's YouTube support to find b-roll he is allowed to use, he edits something, his co-founder leaves notes such as “we need to use this clip instead” and his agent can then apply them. Full-time filmmakers are also using Kino. They tend to resemble “toxenmaxxer” software developers, where 15+ agents iterate on a single project, each trusting Kino as the source of truth for timeline state, graphics, media, everything.
The full editor is free, including unlimited imports and exports, real-time collaboration and MCP access for your own agent. Pro is $25 per editor per month and adds unlimited MCP tool calls, share links, more storage, YouTube search, and the ability to edit alongside your team. You can download it at
https://kino.ai
. We have not yet released Kino for the pure web browser, just Electron for now.
If you make videos personally, if you have ProRes media and you want to try to break Kino, if you have legacy video editor projects to bring in, or if you want to make more content for your company, we'd love to hear how Kino works for you.
