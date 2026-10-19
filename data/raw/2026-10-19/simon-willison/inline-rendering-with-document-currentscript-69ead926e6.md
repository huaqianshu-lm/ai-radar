---
title: "Inline rendering with document​.currentScript"
url: "https://simonwillison.net/2026/Oct/17/document-currentscript/"
source_url: "https://simonwillison.net/2026/Oct/17/document-currentscript/"
canonical_url: "https://simonwillison.net/2026/Oct/17/document-currentscript/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-17T21:11:12+00:00"
fetched_at: "2026-10-19T00:53:41+00:00"
content_type: "markdown"
is_list_page: false
---

Inline rendering with document​.currentScript
Lean Rada describes a neat trick that takes advantage of the
document.currentScript
property. You can use that to drop in a tiny inline
<script>
element that replaces itself when the page loads:
The year is <script>
document.currentScript.replaceWith(
  new Date().getFullYear())</script>
If you define a shortcut function like this:
$=(...n)=>document.currentScript.replaceWith(...n)
You get a tiny template language:
The year is <script>$(new Date().getFullYear())</script>
Tags:
javascript
