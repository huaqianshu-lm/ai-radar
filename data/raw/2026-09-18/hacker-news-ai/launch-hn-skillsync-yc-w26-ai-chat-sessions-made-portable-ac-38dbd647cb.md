---
title: "Launch HN: Skillsync (YC W26) – AI chat sessions made portable across agents"
url: "https://news.ycombinator.com/item?id=49743049"
source_url: "https://news.ycombinator.com/item?id=49743049"
canonical_url: "https://news.ycombinator.com/item?id=49743049"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-17T16:22:15+00:00"
fetched_at: "2026-09-18T01:05:20+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49743049
Author: cat-whisperer
Score: 46

Hey HN, we're Nars & Nishant, founders of Skillsync (
https://skillsync.com
)
Skillsync lets you move your AI chats across every coding agent. Most of our work exists as conversations, which are currently scattered across our agents. Though stored locally, these conversations use different formats. This is annoying because you cannot simply switch between agents without starting over. We get locked into a single provider and their agent as we invest in skills and memories over time. Skillsync acts as a universal converter. It moves the entire session, including all the messages, reasoning and tool calls so you can pick up right where you left off.
Skillsync collects all your sessions in one place and makes them searchable. It breaks down what each session is carrying, including which loaded skills the agent is actually using, making stale context easy to spot. You can also create shared workspaces to sync sessions across your team. You can build your own closed loop systems. Everything runs locally except when you share to workspaces.
The core is an open-source Rust engine called txcript (
https://github.com/skillsynchq/txcript
). It translates a session from one agent's on-disk format into another's, mapping conversation, reasoning, and tool history. Think ffmpeg or pandoc, but for agent sessions.
On top of that engine is a local-first desktop app. Your agent sessions are normally scattered across different tools' folders in formats you'd never read by hand; the app surfaces them in one place with a UI that makes them actually readable, the conversation, the reasoning, and the tool calls, so you can revisit what happened, move a session into another agent, or share it with a teammate.
Skills and memory are stored as portable, human-readable markdown you own, and exposed to any agent over MCP for search and selective retrieval.
Sessions and translation run locally on your machine. The one thing that leaves is what you explicitly share into a team workspace.
It’s been surprising to us to see how locked-in people already are without realizing it. You don't notice you're trapped in one agent or harness until you try to leave, and by then you've got months of sessions stuck in a format only that tool can read. The lock-in is invisible right up until it's expensive.
Once sessions are portable, they stop being disposable logs and become something you can actually build on, spotting patterns in how you work, handing a session off to someone else, letting a non-technical teammate pick up where an engineer left off. The session turns out to be the unit of collaboration, and right now it's being thrown away.
Before Skillsync, Nars and I built an open-source payment orchestrator that let merchants route across many processors instead of getting locked into one (30k+ GitHub stars). Fighting vendor lock-in by making incompatible systems interoperate was the whole job. We came into YC with a different idea, but the more we lived inside coding agents the more we saw the same problem from the other side: your context is locked into whatever agent you start with, because every agent stores sessions differently and none of it moves.
Some of the things we’re seeing people do with Skillsync are:
- Moving a session between Claude Code, Codex, and Cursor mid-task, including when you hit a usage limit on one and want to keep going on another.
- Thinking through a problem in a browser Claude chat, then handing the whole thread to Claude Code or Codex to build.
- Sharing research sessions with a team. Everyone uploads their sessions, so teammates and their agents can build on each other's work instead of repeating it.
It's available as a Mac app, CLI and MCP. Here's the demo:
https://youtu.be/7hVhSnSKGl8
. Would love to hear your feedback and answer questions!
