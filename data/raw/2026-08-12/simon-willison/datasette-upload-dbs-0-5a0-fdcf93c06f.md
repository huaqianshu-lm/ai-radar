---
title: "datasette-upload-dbs 0.5a0"
url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything"
source_url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything"
canonical_url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-08-11T20:35:13+00:00"
fetched_at: "2026-08-12T15:13:25+00:00"
content_type: "markdown"
is_list_page: false
---

Release:
datasette-upload-dbs 0.5a0
This plugin has been around for a while - it lets users upload a brand new SQLite database to a hosted Datasette instance, at which point that database will start being served by that instance.
It can also be used to atomically swap a database with a more recent version. The uploaded database is saved to a file, verified, then swapped in so
/name
starts serving the new one.
The new release adds a formalized API, so you can replace an existing database (or add a new one) like this:
curl -X POST \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Accept: application/json" \
  -F "db=@content.db" \
  -F "db_name=content" \
  https://your-instance.example.com/-/upload-dbs
This means you can build fresh databases in an environment such as GitHub Actions and swap them in production as soon as that build has completed.
Tags:
datasette
