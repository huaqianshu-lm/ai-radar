---
title: "Show HN: Spotatui, a Spotify TUI/GUI without web API rate limits"
url: "https://github.com/LargeModGames/spotatui"
source_url: "https://news.ycombinator.com/item?id=50070010"
canonical_url: "https://github.com/LargeModGames/spotatui"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-13T11:32:00+00:00"
fetched_at: "2026-10-14T01:40:08+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50070010
Original URL: https://github.com/LargeModGames/spotatui
Author: LargeModGames
Score: 48

About 11 months ago i revived the amazing but unfortunately unmaintained spotify-tui. Since then I have been working on it almost non stop, finding a lot of problems on the way.
One of the main issues I ran into were the Spotify web API rate limits. Third party clients like spotatui are dependent on a developer app made in the Spotify developer dashboard, which get rate limited a lot and Spotify has slowly been deprecating endpoints from it. The workaround for this used to be using a shared client id from ncspot but unfortunately that got rate limited too. This is when i started adding other playback sources, including YouTube, Navidrome/Subsonic, Internet radio with +- 30.000 stations, local files, Qobuz for lossless audio and Apple Music for macOS only where it controls the music app remotely.
I fixed both the deprecated endpoints and the rate limits with one solution. It still uses librespot in the back, my spotatui specific fork, but gets all data from it instead of only playback. The data comes from the internal API of the official clients, that API gives metadata, playlists, the user library, devices, lyrics and audio analysis. For searching it uses Pathfinder, the internal GraphQL API.
There are no web API rate limits because there is no shared app quota. Every user uses their own session as if it was the official client. The only potential problem is that Spotify does not document this API so any change on their side would break it. I intend to fix any of those issues as soon as they pop up.
It all started as a TUI back in 2019 but since then I've added a GUI to it too. The GUI is still a bit behind the TUI in terms of features, it only ships Spotify for now, but full parity between the TUI and GUI is coming soon. After that full parity with the official client is next. That is also why I made the GUI looks almost the same as the official client. That way its easier for me and users to find missing features.
Spotatui also has lua scripting support, a optional Web companion on spotatui.com, and if you have a AI coding agent like ChatGPT codex or Claude Code you can enable the MCP tools, which lets AI become your personal DJ just by talking to it.
Its written in Rust, uses ratatui for the terminal UI and Tauri 2 for the GUI. The Rust core starts a small web server with localhost that only your pc can reach which the GUI then serves. Both frontends share the same playback logic, the same login and the same Spotify code. The only difference is how you interact with it.
On first launch it opens a web browser where you need to login with your Spotify premium account (premium is not optional), that is the whole setup done. I would love any feedback about bugs you encounter or features you would like to see.
GitHub:
https://github.com/LargeModGames/spotatui
Releases:
https://github.com/LargeModGames/spotatui/releases/latest
Website:
https://spotatui.com/
Thanks to librespot for making this all possible
