---
title: "datasette-agent 0.7a1"
url: "https://simonwillison.net/2026/Nov/24/datasette-agent/"
source_url: "https://simonwillison.net/2026/Nov/24/datasette-agent/"
canonical_url: "https://simonwillison.net/2026/Nov/24/datasette-agent/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-24T03:45:57+00:00"
fetched_at: "2026-11-25T05:15:31+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-agent 0.7a1
A small improvement to
Datasette Agent
: chat sessions could already open an iframe side panel that could then navigate to different pages. This version improves navigation by fragment hashes, for deeper integration with other Datasette plugins that update fragment hashes when the user interacts with the plugin in a way that changes state.
I built this in order to fix some bugs with the much more exciting
datasette-charts 0.2a0 release
.
Tags:
datasette-agent
,
datasette
