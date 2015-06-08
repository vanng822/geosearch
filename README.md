## Geosearch

Index and search on data containing geo-point within a circle.
It uses RTree and SpatialIndex for looking for items inside bbox.
Radius filter is applied further on result if needed.


## Install deps

### libspatialindex

	cd deps/spatialindex-src-1.8.5
	./configure
	make
	make install
	
You may need to run sudo and make sure install-sh executable

### install Python packages
	
	pip install -r requirements.txt
	

## Running
	
### Building the index
	
	mkdir index
	python indexer.py

this can take sometimes

### Running api

	python runserver.py
	
### Running client

	cd client
	python -m SimpleHTTPServer

## Running tests
	
	py.test tests