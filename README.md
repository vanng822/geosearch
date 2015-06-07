## Geosearch

Index and search on data containing geo-point.
It uses RTree and SpatialIndex for looking for items inside bbox.
Distance filter is applied further on result if needed.


## Install deps

	cd deps/spatialindex-src-1.8.5
	./configure
	make
	make install
	
You may need to run sudo and make sure install-sh executable
