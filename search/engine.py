# -*- coding: utf-8 -*-

import rtree
from utils import get_bbox
from filters import RadiusFilter
from sorting import sort_by_popularity

    
class Engine(object):

    def __init__(self, index_name='index/products', strict_radius=True):
        # index for geo-spatial search
        self.index_name = index_name
        self.idx = rtree.index.Rtree(self.index_name)
        self.strict_radius = strict_radius

    def find(self, lng, lat, radius, count=10, filters=None, sort_func=sort_by_popularity):
        
        left, bottom, right, top = get_bbox(lng, lat, radius)
        #print left, bottom, right, top

        items = self.idx.intersection((left, bottom, right, top),
                                         objects=True)

        result = [item.object for item in items]
        
        if self.strict_radius:
            radius_filter = RadiusFilter(lng, lat, radius)
            result = radius_filter.apply(result)
            
        if filters is not None:
            for filt in filters:
                result = filt.apply(result)
        
        if sort_func:
            result = sort_func(result)

        return result[:count]
