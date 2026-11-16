---
title: "datasette 0.65.6"
url: "https://simonwillison.net/2026/Nov/15/datasette-2/"
source_url: "https://simonwillison.net/2026/Nov/15/datasette-2/"
canonical_url: "https://simonwillison.net/2026/Nov/15/datasette-2/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-15T23:18:17+00:00"
fetched_at: "2026-11-16T02:36:10+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette 0.65.6
I backported a minor security fix from 1.0a43:
Fixed a security issue where a database registered using
add_database(db, name=..., route=...)
with a route that differs from its name could be downloaded from
/<route>.db
by actors who were denied access to it. [...]
Tags:
security
,
datasette
