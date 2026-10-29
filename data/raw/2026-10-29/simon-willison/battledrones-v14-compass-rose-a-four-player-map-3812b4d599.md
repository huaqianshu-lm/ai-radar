---
title: "battledrones v14: Compass Rose, a four player map"
url: "https://simonwillison.net/2026/Oct/24/battledrones/"
source_url: "https://simonwillison.net/2026/Oct/24/battledrones/"
canonical_url: "https://simonwillison.net/2026/Oct/24/battledrones/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-10-24T03:59:57+00:00"
fetched_at: "2026-10-29T02:11:18+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
battledrones v14: Compass Rose, a four player map
I added four player online mode to
Battledrones
- previous maps were limited to two.
Here's the initial prompt I used:
Add a new map for a four player battle - four way rotational symmetry, up to four AI players, works with the WebSocket non-audio based multiplayer mode so up to four human players can join (any spare slots use AI)
Claude Opus 5.5 added a new map called "Compass Rose" and modified the WebSockets multiplayer network code to support up to four players for that map, joining via share links or QR codes.
The new teams use robots themed in purple and green, joining the existing blue and red designs. You can preview those colors in
the updated model browser
.
Here's
a replay link
to watch a four way AI battle with the "Goliath Armada" mutator turned on, where each side starts with four giant Goliath mech units.
Tags:
game-design
,
projects
,
claude
