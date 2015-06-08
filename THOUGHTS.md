Use geospatial search to find interested stores in the bounding box,
since most implementation out there support bbox. If we have to filter
down to radie we can filter the result again.

Now when we have all stores we pick up all products

- Index stores on their coordinates, together with id
- Index/hash stores on id
- Index/hash product on store id