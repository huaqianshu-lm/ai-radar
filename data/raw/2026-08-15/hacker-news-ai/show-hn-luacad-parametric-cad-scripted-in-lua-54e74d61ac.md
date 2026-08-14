---
title: "Show HN: LuaCAD – Parametric CAD Scripted in Lua"
url: "https://luacad.ad-si.com"
source_url: "https://news.ycombinator.com/item?id=49301215"
canonical_url: "https://luacad.ad-si.com"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-14T16:43:22+00:00"
fetched_at: "2026-08-14T23:23:01+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49301215
Original URL: https://luacad.ad-si.com
Author: adius
Score: 63

LuaCAD models solids in Lua rather than the OpenSCAD language, with operator
overloading for CSG (`a + b`, `a - b`, `a * b`).
It ships with a CLI and a desktop app, including a preview area and a text editor.
I've always been a big fan of OpenSCAD, but the SCAD language itself is unfortunately quite cobbled-together and is a very poorly designed programming language.
LuaCAD takes all the good parts of OpenSCAD and combines them with one of the best scripting languages. It has now completely replaced OpenSCAD for me, and I think it provides a better experience than OpenSCAD for all use cases. I'd love to hear any reasons why LuaCAD shouldn't fully replace OpenSCAD!
It’s fully open source and you can find the repo here:
https://github.com/ad-si/LuaCAD
Tech stack:
- It's implemented in Rust and uses mlua (
https://github.com/mlua-rs/mlua
) to execute the Lua code.
- Uses OpenCSG (
https://opencsg.org
) for fast and correct rendering of the 3D models (like OpenSCAD)
- Uses Manifold (
https://github.com/elalish/manifold
) to create the manifold triangle meshes
- Native support for all BOSL2 functions (i.e. implemented in Rust for better performance)
