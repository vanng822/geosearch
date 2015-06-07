# -*- coding: utf-8 -*-

import rtree
from utils import get_bbox
from filters import RadiusFilter


class Engine(object):

    def __init__(self, index_name='index/products', strict_radius=True):
        # index for geo-spatial search
        self.index_name = index_name
        self.idx = rtree.index.Rtree(self.index_name)
        self.strict_radius = strict_radius

    def find(self, lng, lat, radius, count=10, filters=None, sort_func=None):
        """ find will search for entity that located within circle of radius

            It uses bbox model to look for all entities
            If all entities must be inside the circle it will
            filter out items by applying further calculation

            Args:
                lng: longitude of geopoint
                lat: latitude of geopoint
                radius: distance from geopoint in meters
                count: number of items to return
                filters: list of filters implementing Filter
                sort_func: function(items) for sorting
            Returns:
                list of items

        """
        left, bottom, right, top = get_bbox(lng, lat, radius)
        # print left, bottom, right, top

        items = self.idx.intersection((left, bottom, right, top),
                                      objects=True)

        result = [item.object for item in items]

        if self.strict_radius:
            radius_filter = RadiusFilter(lng, lat, radius)
            result = radius_filter.apply(result)

        if filters is not None:
            for filt in filters:
                result = filt.apply(result)

        if sort_func is not None:
            result = sort_func(result)

        return result[:count]
