---
title: "datasette-mcp 0.2"
url: "https://simonwillison.net/2026/Sep/1/datasette-mcp/"
source_url: "https://simonwillison.net/2026/Sep/1/datasette-mcp/"
canonical_url: "https://simonwillison.net/2026/Sep/1/datasette-mcp/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-09-01T15:30:12+00:00"
fetched_at: "2026-09-03T00:59:16+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-mcp 0.2
"rows"
from
execute_sql
is now an array of objects. Previously it was an array of arrays. This should help weaker models avoid losing track of which positional array element maps to which column.
#1
Now depends on
mcp>=2.1.1
.
This is the first non-alpha release of the plugin. I'm confident it's ready as I've been using it quite a bit myself.
Tags:
datasette
,
model-context-protocol
