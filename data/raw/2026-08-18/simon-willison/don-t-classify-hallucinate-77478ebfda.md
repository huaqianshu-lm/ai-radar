---
title: "Don't classify. Hallucinate!"
url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
source_url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
canonical_url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-08-14T21:54:35+00:00"
fetched_at: "2026-08-17T23:23:45+00:00"
content_type: "markdown"
is_list_page: false
---

Don't classify. Hallucinate!
I still have quite a bit of older content on my blog that I never got round to tagging. My blog has
1,856 tags
- likely too many to feed to an LLM in one go and say "which of these tags match the following content".
Doug Turnbull has a neat solution. Tell the model to output tags without any details of the existing vocabulary, then use vector embeddings against the existing corpus to find the concrete tags that are closest to the ones the model imagined might fit!
His example prompt suggests including an example of the shape of your tags to help the model make a more useful guess:
Your task is to create novel, never seen before, furniture, home goods, or hardware classification that best fit a search query.
Product classifications might look like:
Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables
Décor & Pillows / Decorative Pillows & Blankets / Throw Pillows
Furniture / Bedroom Furniture / Dressers & Chests
Kitchen & Tabletop / Kitchen Organization / Food Storage & Canisters
School Furniture and Supplies / School Furniture / School Chairs & Seating / Stackable Chairs
Baby & Kids / Toddler & Kids Bedroom Furniture / Kids Beds
Here's the query to generate classifications for:
brown coffee table
Tags:
search
,
ai
,
generative-ai
,
llms
,
embeddings
,
doug-turnbull
