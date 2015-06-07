# -*- coding: utf-8 -*-


class Product(object):

    """ Model for holding product info including
        store geolocation and tags

        Main purpose is for indexing and return to client

    """
    # id,shop_id,title,popularity,quantity

    def __init__(self, id, shop_id, title, popularity, quantity, lng, lat, tags=None):
        # store coordinates
        self.lng = lng
        self.lat = lat
        # product
        self.id = id
        self.shop_id = shop_id
        self.title = title
        self.popularity = float(popularity)
        self.quantity = float(quantity)
        if tags is None:
            tags = []
        self.tags = tags

    def to_dict(self):
        """ Return a dict for json to client

        """
        return {
            'id': self.id,
            'title': self.title,
            'popularity': self.popularity,
            'quantity': self.quantity,
            'shop': {  # weirdo to have shop inside product
                'id': self.shop_id,
                'lng': self.lng,
                'lat': self.lat
            }
        }
