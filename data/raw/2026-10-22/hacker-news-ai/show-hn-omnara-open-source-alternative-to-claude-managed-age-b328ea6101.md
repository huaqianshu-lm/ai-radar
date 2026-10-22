---
title: "Show HN: Omnara – Open-Source Alternative to Claude Managed Agents"
url: "https://github.com/omnara-ai/omnara"
source_url: "https://news.ycombinator.com/item?id=50183892"
canonical_url: "https://github.com/omnara-ai/omnara"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-21T16:44:53+00:00"
fetched_at: "2026-10-22T01:18:40+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50183892
Original URL: https://github.com/omnara-ai/omnara
Author: kmansm27
Score: 20

Hey y'all, Kartik from Omnara (
https://omnara.com
) here. We're building an open-source API for running durable agents. You create an agent with an API call, and Omnara runs the agent loop, gives the agent sandboxes to run commands in, and handles secrets, permissions, and RBAC. Each agent's state is stored in Postgres, so agents survive restarts and cost nothing while idle. You can message them and stream their events over the API.
You may remember us from our early days, when we made a remote-control phone app for Claude Code and Codex. Since the harness ran on a laptop back then, we had to build a relay to reach it, it stopped when the laptop closed, and moving it to a cloud sandbox meant syncing code and agent state between machines. We didn't think remote-controlling a local agent was end-game for how people would run agents, so we built a new product where the agent runs in the cloud, any client can talk to it through an API, and it can still use your laptop as one of its machines.
Anthropic and OpenAI are building hosted versions of this, like Claude Managed Agents and the OpenAI Agents API. Omnara is an open-source version you can run on your own servers and use your own models. It's basically a harness server like the opencode or codex servers, but durable, scalable, with the usual harness features like file and shell tools, subagents, compaction, permission prompts, MCP, skills, memory, yada yada yada.
Here's some interesting architectural decisions we made while building this out:
Most harnesses, like Claude Code, Codex, OpenCode, Pi, Goose, etc, run the agent loop in one long-lived process that keeps its log in a JSONL or SQLite file. In Omnara, the log is an append-only event log in Postgres, with inputs, model outputs and tool calls stored as typed rows in their own tables. The loop runs on stateless workers in the control plane. A worker runs one iteration of the loop, either a model call or the tool calls it produced, then releases the agent and puts the next iteration on a queue in Postgres. Whichever worker is free picks it up, so each iteration of an agent's loop can run in a different process on a different machine. Each iteration's result commits in one transaction, so the model output, its tool calls, usage and the next wakeup are saved together or not at all. If a worker dies mid-iteration, nothing commits, its lease expires, and another worker retries it. Agents waiting on a user, a tool or a retry don't hold a worker, so one worker can multiplex thousands of agents.
Also unlike other harnesses, the machines that the workers (our agent loop) run on aren't where the agent runs its commands. Instead, any macOS or Linux machine with an internet connection, like your laptop or any cloud sandbox, can run a small daemon (omnarad) that connects out to Omnara, so it doesn't need any open inbound ports. The agent then gets tools for that machine, like running a command or editing a file. An agent can have any number of machines connected to it. A fun thing I like to do is I have my laptop and a cloud sandbox connected to the same agent, so when my laptop is on, my agent codes there and I can interact with it, and I have it often push to Github. When I close my laptop, my agent sees the laptop went offline, pulls the latest changes to its cloud sandbox, and continues there.
The entire codebase is open source at
https://github.com/omnara-ai/omnara
, and it’s self hostable, even on a single machine with docker compose. You can also use the hosted version at
https://omnara.com
. Let me know what you think!
