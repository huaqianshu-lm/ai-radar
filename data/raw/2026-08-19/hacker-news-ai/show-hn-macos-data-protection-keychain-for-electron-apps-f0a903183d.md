---
title: "Show HN: macOS data protection keychain for Electron apps"
url: "https://github.com/biw/keychain-store"
source_url: "https://news.ycombinator.com/item?id=49349159"
canonical_url: "https://github.com/biw/keychain-store"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-18T17:25:19+00:00"
fetched_at: "2026-08-18T23:23:20+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49349159
Original URL: https://github.com/biw/keychain-store
Author: biwills
Score: 21

Hey HN,
I've been working on Hansel [1] (an encrypted personal data store you can query with agents), and there wasn't a good way to use the modern macOS Data Protection Keychain.
Electron's safeStorage [2] uses the legacy file-based keychain, which allows other apps/agents to query it with the `security` CLI. Not great when you have a dozen agents running in the background! The Data Protection Keychain is nice because it limits access via code-signing access groups and lets you set access rules like Touch ID and/or password.
1:
https://hansel.so/
2.
https://www.electronjs.org/docs/latest/api/safe-storage
