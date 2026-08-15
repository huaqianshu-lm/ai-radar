---
title: "sqlite-utils 4.2"
url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
source_url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
canonical_url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-08-13T20:11:29+00:00"
fetched_at: "2026-08-15T23:21:35+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
sqlite-utils 4.2
Lots of improvements in this one relating to the
table.transform() feature
, which adds support for complex alter table operations by creating a fresh table, copying across the data and then dropping and replacing the old one.
transform()
now preserves a much larger array of edge-case schema definitions, including check constraints, unique constraints and even comments describing the columns.
There are also
new introspection properties
for check constraints, and a whole lot of other smaller changes.
Includes contributions from
Bunlong Heng
,
ethanhawkes-gif
,
Rami Abdelrazzaq
,
nyxst4ck
, and
ikatyal2110
.
(It later turned out 4.2 had
a crashing bug
, fixed in
4.2.1
.)
Tags:
releases
,
sqlite
,
sqlite-utils
