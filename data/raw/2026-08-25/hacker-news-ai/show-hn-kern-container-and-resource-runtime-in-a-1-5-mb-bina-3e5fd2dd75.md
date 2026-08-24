---
title: "Show HN: Kern – container and resource runtime in a 1.5 MB binary, no daemon"
url: "https://github.com/getkern/kern"
source_url: "https://news.ycombinator.com/item?id=49423927"
canonical_url: "https://github.com/getkern/kern"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-24T18:24:59+00:00"
fetched_at: "2026-08-24T23:23:10+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49423927
Original URL: https://github.com/getkern/kern
Author: realexweb
Score: 45

I built kern because I needed a fast, zero-daemon tool to set CPU/RAM limits and run isolated tasks without the overhead of Docker. It's a single 1.5MB Rust binary using OCI images, cgroup v2, and namespaces. Boxes start in ~3.5ms. It's not a Kubernetes CRI or a microVM, just a standalone container and resource runtime for CLI and agents.
