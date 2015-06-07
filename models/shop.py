# -*- coding: utf-8 -*-

class Shop(object):

    def __init__(self, id, name, lat, lng, tags=None):
        self.id = id
        self.lng = lng
        self.lat = lat
        self.name = name
        if tags is None:
            tags = []

        # tags should have relation to product not shop
        # since the search is product-based
        self.tags = tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def contains_tag(self, tag):
        return tag in self.tags
