---
title: "Launch HN: Alter (YC S25) – Access control for multi-user agents"
url: "https://alterauth.com/"
source_url: "https://news.ycombinator.com/item?id=50176908"
canonical_url: "https://alterauth.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-21T06:42:12+00:00"
fetched_at: "2026-10-22T01:18:40+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50176908
Original URL: https://alterauth.com/
Author: simfinii
Score: 52

Hi HN! We’re Srikar and Kevan, founders of Alter –
https://alterauth.com/
. We’re building access control for agents that can take actions on behalf of multiple users.
If you’ve built an internal agent people use through Slack, you may have experienced this scenario: everyone signs in with their own account, but the agent connects to the CRM or billing system with one shared API key, so the agent can do anything that the key can do. User-level authentication in Slack does nothing to control what the agent can do in an external system like the CRM or billing system.
Here’s what Alter does:
-It acts as a proxy and manages downstream credentials for every API request that an agent takes;
-It takes identity into account for every action the agent does. Automatically take into account the end user identity of the person that the agent is taking actions on behalf of.
-It enforces fine grained runtime policies and records compliance grade audit logs.
Here’s a demo video:
https://www.youtube.com/watch?v=9ZqPU14ipGE
We started this because we saw first hand how hard it is to build agents in regulated industries. To unlock the true benefits of agents we need to allow agents to take actions, sometimes actions on behalf of end users. I (Srikar) was working at Goldmans and I saw how prohibitively expensive it was for me as a developer to write my own custom auth to enable multi-tenancy in agents and to allow agents to have strict policy controls as they act on behalf of end users. My co-founder, Kevan, is a second time founder and was previously working on a database startup. He has experience building and selling deep tech into highly regulated environments. So this problem seemed like a natural fit for the both of us.
Building and maintaining custom auth for multi tenant agents was challenging. But so was ensuring that the solution we developed was secure, scalable and keeping track of security grade audit logs. As a result we realized there needs to be a separate product category for this that enables developers to easily build secure multi user agents that can actually take actions in an enterprise.
Some of the real-world use cases we’ve seen include:
We have built a multi user open claw for our own team using Alter that saved us countless hours on our GTM effort.  Link here:
https://github.com/AlterAIDev/openclaw-alter-plugin
We have multiple startups who have used our platform to build their own secure internal agents for everything ranging from SRE agents to back office agents dealing with Quickbooks and payroll platforms like Rippling. It has saved developers countless hours both in terms of building and maintenance. We also have a defense contractor building air gapped agents for marine corp using Alter.
Under the hood, the value that we provide is that we do a lot of the plumbing that no one wants to do. We support hundreds of providers, all manually tested end to end. Reliability is our biggest priority. We have built this in a way to allow developers to custom build their agents however they see fit. Everything ranging from custom policies, agent delegation, user attribution, audit logs needed for compliance to a LLM gateway with guardrails (Coming soon)
Building a security product is hard. We have learnt that in order to build a truly secure product, security thinking has to pervade every part of the development process. We have embraced shift left security. Every PR that is pushed out is continuously checked for supply chain attacks, potentially dangerous code patterns etc.
Our business plan revolved around usage based pricing. There is a free tier up to 10k requests and then a pricing tier starting beyond that. We would love it if people configured their APIs and OAuth credentials, tried out the policies and actually built agents that can take actions with alter!
If you’ve built an agent that acts for multiple users, how are you handling permissions today? We’d especially like to hear what you’ve had to build yourself.
https://alterauth.com/
