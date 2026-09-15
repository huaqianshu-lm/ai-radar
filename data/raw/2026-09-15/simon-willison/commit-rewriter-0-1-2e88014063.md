---
title: "commit-rewriter 0.1"
url: "https://simonwillison.net/2026/Sep/14/commit-rewriter/"
source_url: "https://simonwillison.net/2026/Sep/14/commit-rewriter/"
canonical_url: "https://simonwillison.net/2026/Sep/14/commit-rewriter/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-09-14T00:28:10+00:00"
fetched_at: "2026-09-15T01:13:50+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
commit-rewriter 0.1
I built this little web app the other day to help edit the commit messages for the
Datasette security releases
. The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication.
If you want to edit the commit messages for a repository you can run it like this:
uvx commit-rewriter path/to/repo
Omit the path if you are already in the directory for that repo.
When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent.
Tags:
git
,
projects
,
python
,
ai-assisted-programming
