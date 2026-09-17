---
title: "datasette 1.0a40"
url: "https://simonwillison.net/2026/Sep/16/datasette/"
source_url: "https://simonwillison.net/2026/Sep/16/datasette/"
canonical_url: "https://simonwillison.net/2026/Sep/16/datasette/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-09-16T23:51:43+00:00"
fetched_at: "2026-09-17T01:07:10+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette 1.0a40
Same security fix as
0.65.5
, plus some neat new features and bug fixes:
Plugins can now launch and manage
background tasks
using the new
datasette.add_background_task()
method. Thanks,
Alex Garcia
.
I've migrated Datasette to
httpx2
for features like the internal
datasette.client.get()
method.
A whole lot of
bug fixes
, many of them stemming from a recent effort to triage issues for a 1.0 stable release.
Tags:
security
,
datasette
