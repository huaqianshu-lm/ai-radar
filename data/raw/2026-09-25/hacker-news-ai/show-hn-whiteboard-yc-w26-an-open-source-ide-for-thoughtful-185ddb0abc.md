---
title: "Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design"
url: "https://github.com/devdotfast/whiteboard"
source_url: "https://news.ycombinator.com/item?id=49833867"
canonical_url: "https://github.com/devdotfast/whiteboard"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-24T17:21:36+00:00"
fetched_at: "2026-09-25T01:12:09+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49833867
Original URL: https://github.com/devdotfast/whiteboard
Author: sidharthkmenon
Score: 186

Hello! We’re Sid, Alex, Ketan, and Milan. We’re building Whiteboard (
https://whiteboard.dev.fast/
), an open-source desktop app where humans and agents can architect software together in a common workspace. Here’s our repo:
https://github.com/devdotfast/whiteboard
.
We were missing the feeling of a “whiteboard session” with another dev where you leave with a deep understanding of a system, so we built this app for ourselves. Whiteboard plugs into the tools you already use - e.g. Claude Code, Codex, etc. – and gives your agent an SDK to draw on an in-app canvas to describe its work. We began with an MVP based on HTML artifacts and started rethinking the app as we ran into limitations:
1. Built on top of CodeOSS: We found that in pure HTML tools it was hard to connect a spec or diagram to code. In Whiteboard, when you click on visualizations like a sequence diagram, an entity relationship diagram, or a quote from the agent’s trace, you can jump to the underlying code directly. When navigating code, you get keybindings and LSP support from VSCode out of the box. We’ve found this is especially valuable because tradeoffs are often only discovered after a first pass at implementation (re: slop)
2. Semantic diff viewer: we wrote a semantic, AST-aware diff viewer in Rust so you can only view the code changes which are relevant to you [1]. We’ve set up some sane defaults: large added functions are summarized as pseudocode, and things like unit tests and large documentation changes are collapsed / hidden. This is all customizable with a WASM-based plugin system.
3. Decision Log: We found it difficult to reason about what set of decisions our agents made autonomously. So we built tools for agents to query and link their own traces to the Whiteboard, so you can understand how the requirements that you set were implemented, and understand what decisions your agent made autonomously.
Here’s a quick demo video explaining more:
https://www.youtube.com/watch?v=ChPn3ftULWE
Folks at companies like Salesforce and Modal are using Whiteboard today as a review tool for architecture or spec-level changes – really any change where they want to be involved:
1. Reviewing your own coding agent’s work: because Whiteboard makes it easier to review large amounts of code, folks will typically have their AI agents create a prototype and a corresponding Whiteboard session so they can iterate on the design.
2. Reviewing other people’s changes: We’ve found that Whiteboard is particularly helpful when composed with tools like Greptile. For example, you can run an automated code reviewer on small changes and escalate to a Whiteboard session for the changes that require human judgement.
Why we built this: we’re four buddies from college who quit our jobs as tech leads right before agentic coding became industry standard. As we iterated towards an MVP for a previous idea, we struggled to maintain a comprehensible codebase while reaping all the velocity benefits of agentic coding. As more PRs were merged without our understanding, we felt a ‘cognitive debt’ begin to seep in, until it became difficult for us to even contribute to the system [2].
We’re releasing our desktop app under an MIT license. Please poke through and feel free to contribute! Eventually we’ll charge companies for a hosted web version that manages whiteboard session creation alongside features like trajectory storage and multiplayer reviews. Everything will always remain self-hostable.
Thanks for reading, and we hope you try it out! We would love to hear any feedback and to learn from your expertise.
Here’s are the project links again:
https://github.com/devdotfast/whiteboard
, and you can install (for MacOS + Linux) at
https://install.dev.fast
[1] diffs library:
https://github.com/devdotfast/diffr
[2] Credit for the term ‘cognitive debt’ goes to
https://www.geoffreylitt.com/2026/07/02/understanding-is-the...
