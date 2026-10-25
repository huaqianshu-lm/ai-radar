---
title: "eMudhra Intermediate CA Compromise"
url: "https://simonwillison.net/2026/Oct/20/emudhra-certificates/"
source_url: "https://simonwillison.net/2026/Oct/20/emudhra-certificates/"
canonical_url: "https://simonwillison.net/2026/Oct/20/emudhra-certificates/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-20T23:50:25+00:00"
fetched_at: "2026-10-25T00:53:24+00:00"
content_type: "markdown"
is_list_page: false
---

eMudhra Intermediate CA Compromise
This is very, very bad news:
The private keys of eight eMudhra intermediate CA certificates have been compromised. They chain to roots trusted by the Mozilla, Microsoft, Apple and Chrome root programs and by many downstream trust stores.
Any software that bundles a list of trusted certificates needs to be updated. This site is tracking software updates
via this GitHub repository
- Linux distros need to update their
ca-certificates
packages.
In Python world
uv 0.13.4
and
pip 26.2.2
and
certifi 2026.10.19
have been released with upgraded certificate lists.
There's a
very informative thread
about this on the official Python forum.
Tags:
encryption
,
https
,
pip
,
python
,
security
,
uv
