Use geospatial search to find interested items in the bounding box,
since most implementation out there support bbox. If we have to filter
down to radie we can filter the result again. This should work really well
for cases where number of result is not big.

There are couple of geospatial index libs/package where RTree is really interested.
We use RTree instead PyRtree due to performance. Drawback is that you need to build
the c-lib dependency but that should not be to big trouble.

The indexing and searching concept is more generic in this implementation. Indexer will have
freedom to index whatever that can be pickled. Searcher just returns the number of items in
the given bbox. Filtering of items outside the circle is naturally part of the search engine
meanwhile other kind of filters can be defined by the specific application using it.
In this example TagFilter is a specific for Product items. The single sorting function can also
be defined by application.

Stuffs that can be improved at first is multiple indices which one can switch between
when indexing new data. Alternative could be that we have multiple instance which we can
stay on one leg while switching to new index.


Note also that the choice of Product as indexing item is for generic and for easier searching
and post-processing of data. Also didn't expected that the test data was this tight,
23214 items within 1km radius are a lot. This causes a performance hit due to big number of items hit.

If you implement for this specific dataset you should choose to index only the shops
based on coordinates and then have a second index/hash based on shop id for the products.
This case one can search for shops within given circle, filtered by tag,
and then pick up products for further processing. This could be faster.