---
title: "Show HN: Godot and Rust based multiplexer (terminal panes and more)"
url: "https://github.com/godot-pty/gpty"
source_url: "https://news.ycombinator.com/item?id=49660676"
canonical_url: "https://github.com/godot-pty/gpty"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-11T16:03:05+00:00"
fetched_at: "2026-09-12T00:56:39+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49660676
Original URL: https://github.com/godot-pty/gpty
Author: 1nv1n
Score: 78

I wanted to share my side-project: gPTY. Started off as an idea to combine Godot and Rust in a project (two stacks I wanted to use more to learn more). The base inspiration was tmux - simply allow spawning multiple PTYs and then let the user grid/tile them how they see fit.
But since we have the Godot game engine at our disposal, we can do some more interesting things, like add an FPS counter, and then subsequently also let people set their preferred FPS (the idea being the potential lower power draw if someone's running it on a laptop on battery power vs someone running it on a desktop with high/native FPS). In its current state, with me using Oh-my-Pi a lot, it's evolving into a terminal workspace that can be used for orchestrating autonomous AI agents by way of dogfooding (or you know, just run herdr inside of gPTY - it's the better orchestrator and just good software - I found it after starting this project, and now I'm finding myself using it a lot).
Also, we're not limited to just terminals. Since we have Godot, we have basically a 2D (and potentially a 3D) canvas to play with. We can already full-screen the app for "zen" mode, no taskbar, no distractions. TUI die-hards can have their media or other apps entirely in terminal panes.
There has been some ground-work on getting Markdowns displayed properly done and I want to work on some kind of Wiki framework for local knowledge-management next, then create more types of panes (think native audio/video on a media pane, that sits alongside your terminal pane), and some simple 2D games (like snake) to prototype. More details are on the ROADMAP.
What's not easy (and probably won't happen) is a browser. Having done a couple of (small) projects using Electron already, the temptation to ditch Godot/Rust (learning curve) did come up (and also the ecosystem, the ease with which I could pull components and use web technologies - development velocity would definitely be higher there). But on the flipside, given all of the available LLM and AI support that we are privileged to have today, I figured the velocity should be comparable depending on how much I leaned on those. And lean I did.
Godot/Rust seemed the better call to me and my intent anyway - going with the 'it's not just the end but the journey that matters' philosophy. So yes, there has been heavy use of LLMs & AI to generate a lot of the code. But I do review and steer actively, not relying solely on vibes, and there's a few bits here & there that have been human authored.
There are definitely a lot of polish and QoL items that need to land to make the end user experience better, but in the meantime, let me know your thoughts and/or concerns!
Repository:
https://github.com/godot-pty/gpty
Docs/Blog:
https://godot-pty.github.io/gpty/
