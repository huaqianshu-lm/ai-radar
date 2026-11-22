---
title: "datasette-arrows 0.1a0"
url: "https://simonwillison.net/2026/Nov/18/datasette-arrows/"
source_url: "https://simonwillison.net/2026/Nov/18/datasette-arrows/"
canonical_url: "https://simonwillison.net/2026/Nov/18/datasette-arrows/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-11-18T17:09:59+00:00"
fetched_at: "2026-11-22T02:51:43+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-arrows 0.1a0
Datasette 1.0a43
added the ability for plugins to implement streaming export formats. Datasette core supports streaming CSV and TSV - you can export millions of lines of data from a table without needing to load it all into memory, because those two file formats support streaming data in chunks. The
register_output_renderer()
plugin hook can now be used to implement the same pattern for other formats.
I've learned never to release a new plugin feature without accompanying it with a plugin that uses it.
Claude Fable 5.2 suggested the
Apache Arrow streaming
format as a good option, and built this plugin in almost a single shot.
Add the plugin to Datasette (
datasette install datasette-arrows
) and the export dialog gains this new Arrow option:
This screenshot is from Datasette's
main
branch - the most recent release doesn't yet group streaming formats such as Arrow with the TSV and CSV in the "All rows in this table" section, but that's coming in the next alpha release.
Tags:
datasette
,
projects
