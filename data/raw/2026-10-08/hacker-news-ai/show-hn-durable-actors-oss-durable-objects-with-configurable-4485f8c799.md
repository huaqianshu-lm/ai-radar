---
title: "Show HN: Durable Actors – OSS Durable Objects with configurable compute"
url: "https://github.com/TerseAI/durable-actors"
source_url: "https://news.ycombinator.com/item?id=49980399"
canonical_url: "https://github.com/TerseAI/durable-actors"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-06T15:58:19+00:00"
fetched_at: "2026-10-08T02:35:04+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49980399
Original URL: https://github.com/TerseAI/durable-actors
Author: thomask1995
Score: 33

Hi HN, we're Thomas and Olivier from Terse (
https://www.useterse.ai/
) We've built Durable Actors, an open-source alternative to Cloudflare's Durable Objects.
A Durable Object/Actor is a tiny server that handles one request at a time and has its own SQLite database. There's exactly one of each in the world and it is addressed by name.
This is the perfect primitive for deploying multiplayer agents. Each agent can have its own Durable Actor, and each user can connect to that Actor via websocket. This is fully horizontally scalable. Your users can deploy and share agents at will without putting pressure on a central DB or websocket server.
Durable Actors are also great for coordinating agents within a system. Since only one request is handled at a time, you can protect critical data such as a CRM and allow multiple agents to run concurrently without worrying about data races.
The only alternative to this is Cloudflare's Durable Objects. However, there is extreme lock in (they pull you into D1, R2 + workers as well) and it wasn't originally built for agentic workfloads when it was released 5 years ago.
Some notable projects built on Durable Objects include RampInspect, OpenInspect as well as the multiplayer frameworks Liveblocks and PartyKit. You can now build these kinds of projects on Durable Actors.
Durable Actors is a version of DO that is built for concurrent agentic workloads. It is fully open source (MIT License) and includes a helm chart for you to easily self-host.
Some key features:
- Configurable compute: Specify CPU, RAM, data residency, idle-timeouts all in a decorator
- No outer worker: We generate a type-safe client that you can just plug into your existing tech stack.
- (coming soon, like today) Export SQLite table via CLI + MCP for exposing OLTP logs to your agent to help you debug.
And our Performance Numbers (all p95):
- Durable write: 85.6ms
- Stateful Read (data in sqlite): 2.14ms
- Actor Warm up: 334ms
Here is a little counter demo so you can see the latency yourself:
https://demo.useterse.ai/
Would love your feedback!
