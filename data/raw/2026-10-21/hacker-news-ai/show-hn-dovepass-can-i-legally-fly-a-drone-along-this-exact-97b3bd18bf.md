---
title: "Show HN: Dovepass – can I legally fly a drone along this exact path in SF?"
url: "https://dovepass.com"
source_url: "https://news.ycombinator.com/item?id=50156779"
canonical_url: "https://dovepass.com"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-19T19:21:56+00:00"
fetched_at: "2026-10-21T01:22:03+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50156779
Original URL: https://dovepass.com
Author: nimitmehra
Score: 13

Dovepass answers one question for drone operators: given two points, can a drone legally fly between the two points?
I build route planning for delivery drivers and wanted to check what it would look like if the vehicle flies. Drone navigation is different from land-based vehicle navigation. In addition to road and traffic data, it requires data on buildings, building height, wind speed and direction, and total load, including the payload a drone might carry. It is also governed by a set of rules; depending on the area, federal, state, or county rules may apply.
The decision point becomes whether, at each point on the route the drone can fly based upon whether regulations permit, the wind direction favours it and whether it flying over a road or people? Depending on when the drone flies, the same path valid two hours ago may no longer be valid.
For example a trip from 24th & Valencia ( Mission) to 19th Ave & Irving (Inner Sunset) and back is 5.1 km each way. A DJI mini 4 Pro would take 19 min on 7 mph winds from the west and use 92% of its usable battery and give a Go signal with warning. But at 11mph wind from the same direction would become No-Go because it would use 111% of its usable battery. Or whenever there is a Giants game at Oracle Park, this route is unusable because it is 2.5miles from the stadium. FAA bars all drones within 3 nautical miles from a stadium from 1 hour before the game to one hour after it ends.
I chose San Francisco as the first city to build this because there is enough data about the buildings (92% coverage), wind data is easily available at the drone flying height, and the city has a mix of slopes, water bodies, buildings and airport-related airspace restrictions all in one city. The city also has local rules regarding drone flights in parks - both operated by the city as well as by Golden Gate National recreational areas ( National Park Service).
I used kimi to build it and claude acted a sa judge. To understand more about the challenges faced during the build and the tradeoffs made please read -
https://dovepass.com/how-it-was-built/
"
