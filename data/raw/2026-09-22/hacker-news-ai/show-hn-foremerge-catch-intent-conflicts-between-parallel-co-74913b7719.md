---
title: "Show HN: Foremerge – Catch intent conflicts between parallel coding agents"
url: "https://github.com/naw103/foremerge"
source_url: "https://news.ycombinator.com/item?id=49789356"
canonical_url: "https://github.com/naw103/foremerge"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-21T16:22:06+00:00"
fetched_at: "2026-09-22T01:28:29+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49789356
Original URL: https://github.com/naw103/foremerge
Author: naw103
Score: 37

At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time, the failures that hurt the most are when multiple plans or tickets cause architecture changes that cannot both be true. Ex. one agent replaces a class while another one is in the process of extending it. Git only notices if the resulting patches happen to touch the same lines and the review only catches it if they are familiar with both tickets.
Foremerge is a local "git like" coordination layer that sits above git (ie. does not interact with or change the way git and worktrees function), Before editing each agent publishes an intent and the scopes it will change, with the operation it plans to complete on each one.
foremerge intent publish --agent "$A" \
        --summary "Replace PaymentService with StripePaymentService" \
        --scope symbol:PaymentService=replace
    foremerge intent publish --agent "$B" \
        --summary "Add PayPal support to PaymentService" \
        --scope symbol:PaymentService=extend
The publish by the 2nd agent returns a HIGH destructive_vs_additive finding before writing any code. Agents keep their own worktrees and the shared state is one SQLite file in gits common direectory. No hooks, no merge drivers, nothing rewrites your history.
It ships as one Rust binary with a CLI and MCP server with 18 tools and `foremerge setup all` wires it into Claude Code, Codex and Cursor. Because the protocol has nothing provider specific, a Claude agent and a Codex agent coordinate through the same store. Before any work is accepted, Foremerge runs a named check that you configured against the exact git state of the change. An agent that says tests pass is recorded but it dosnt satisfy the acceptance gate without running the check itself.
Detection is deterministic, no judge model reading your code. HIGH conflicts are only asserted for declared operations, ie. matches inferred from prose cap out below high. Claims are advisory leases, not locks so two agents can still hold the same scope without deadlock. The open source version is single matching and so not a distributed consensus.
We have tested this up to 98 parallel agents all working on the same repo with zero conflicts (was supposed to be 100 but 2 agents failed to run due to resource limitations)
I replayed 76 intents on my own agents from a build last week in the order they happened. The sample had exactly 1 conflict (which was flagged) and the review found a blind spot where one agent claimed scope by class name and the other claimed it by an internal method. We are working on fixing that for the next release.
Setup is a 30s install by pasting the quickstart instructions from the readme.md into your agent or manually: 
`curl -fsSL
https://foremerge.com/install.sh
| sh` or `cargo install
--locked foremerge`, then `foremerge init && foremerge setup all` in a repo.
Apache-2.0.
The feedback I want most is which conflicts between your agents plans would you actually want flagged and which would you tollerate as noise?
Repo here:
https://github.com/naw103/foremerge
Website:
https://foremerge.com
More information on the problems this solves:
https://foremerge.com/blog/
