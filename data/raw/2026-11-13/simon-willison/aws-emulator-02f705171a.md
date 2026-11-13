---
title: "aws-emulator"
url: "https://simonwillison.net/2026/Nov/11/aws-emulator/"
source_url: "https://simonwillison.net/2026/Nov/11/aws-emulator/"
canonical_url: "https://simonwillison.net/2026/Nov/11/aws-emulator/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-11T21:18:30+00:00"
fetched_at: "2026-11-13T03:13:32+00:00"
content_type: "markdown"
is_list_page: false
---

aws-emulator
Finally, an official emulator from AWS to run tests against a local clone of their many different services without having to provision a paid API key to do so.
It's written in Rust by a huge swarm of agents - 29,684 commits in the first three weeks of the project. Swaminathan (Swami) Sivasubramanian wrote about
how it came to be
in a guest post on Werner Vogels' blog.
It currently requires Docker to run on macOS or Windows. I'm hoping they fix that in the future - it would be great if you could download a single binary and use that as part of a standard test suite in other languages and on other platforms.
Tags:
amazon
,
amazon-web-services
,
testing
,
werner-vogels
,
ai
,
rust
,
docker
,
generative-ai
,
llms
,
agentic-engineering
