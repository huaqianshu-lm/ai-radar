---
title: "datasette-apps 0.4a0"
url: "https://simonwillison.net/2026/Nov/15/datasette-apps/"
source_url: "https://simonwillison.net/2026/Nov/15/datasette-apps/"
canonical_url: "https://simonwillison.net/2026/Nov/15/datasette-apps/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-15T04:02:45+00:00"
fetched_at: "2026-11-17T04:58:19+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-apps 0.4a0
Datasette Apps are sandboxed HTML and JavaScript applications that live inside Datasette - think Claude Artifacts, but these ones can run SQL queries against your data.
0.4a0 adds support for linking: you can link to an app with
#fragments
in the URL and the app can see and use those, plus supported URL schemes are reported back to Datasette Agent so it can help write apps that link to each other.
This means you can have e.g. an app that shows details about a specific record, and a completely separate app that searches those records and links to their representations in the first app.
Tags:
datasette-agent
,
datasette-apps
,
datasette
,
urls
