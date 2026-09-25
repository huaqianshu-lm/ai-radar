---
title: "Show HN: Critic – Review code with the agent that wrote it"
url: "https://www.critic.run/"
source_url: "https://news.ycombinator.com/item?id=49834098"
canonical_url: "https://www.critic.run/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-24T17:35:28+00:00"
fetched_at: "2026-09-25T01:12:09+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49834098
Original URL: https://www.critic.run/
Author: snyy
Score: 7

Hey HN, I'm Shreyash from Feyn. We help companies build custom models from their data. Today we're releasing Critic, a change review platform that lets you engage directly with the AI that wrote the code.
Agents write most of our code. While that has made us more productive, understanding a change and its consequences has become incredibly difficult. As our company adopted more agentic tools, we found it harder to loop people in on the impact of a PR and the state of a project. We built Critic to fix this.
Critic lets AI agents present their code, annotate key blocks, and include relevant evidence (like screenshots and instructions to run locally).  Anyone viewing that change can talk directly to the agent that wrote it. See a demo here:
https://www.youtube.com/watch?v=U2--lytmOtQ
.
Critic works through a plugin for Codex or Claude Code. When your agent writes code, the plugin asks it to also write a narrative describing the story behind the change, and highlight any assumptions, decisions, or complex code. You can then view the change at critic.run or have your agent pull it via the bundled MCP. Every feature in Critic is available over MCP, so your agent gets all the same context without leaving its harness.
From the dashboard or MCP, you can chat with the authoring agent directly. When Critic receives a question, it forks the authoring session and forwards your question there. That way your main thread stays clean and keeps working.
Local changes are visible only to the owner. Anything pushed to GitHub is mirrored and visible to anyone with permission to view that change on GitHub.
When building Critic, security was a big priority for us. AI agents often run in auto mode and can take many actions on your computer. We wanted to ensure that giving people access to your agent doesn't mean giving them access to your computer. All Critic forked sessions are stripped of their write tools. They can only answer questions about the change and in-progress work in that workspace.
Critic has helped us catch several incidents before they hit production. The most common is a model not reusing artifacts, like existing styles, components, or functions. Because it's so easy to dig into an agent's work and question it, we've also caught more cases of models misdiagnosing issues or writing unhelpful code. Since Critic's UI is faster and friendlier to agents than GitHub, our team is returning feedback quicker as well.
Critic is free to use. Sign up at
https://critic.run
. Let me know if you have feedback or questions.
