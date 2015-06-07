from utils import get_distance


class Filter(object):

    def apply(self, items):
        """ Implementing specific filter task on result

            Args:
                result: list of result items

            Returns:
                list of filtered items

        """
        raise NotImplementedError()


class RadiusFilter(Filter):

    """ RadiusFilter refine the search result

        It will calculate and take only items within radius

    """

    def __init__(self, lng, lat, radius):
        self.lng = lng
        self.lat = lat
        self.radius = radius

    def apply(self, items):
        result = []
        for item in items:
            if (get_distance(self.lng, self.lat, item.lng, item.lat)
                    <= self.radius):
                result.append(item)

        return result


class TagFilter(Filter):

    def __init__(self, tags):
        self.tags = tags

    def apply(self, products):
        result = []
        for product in products:
            hit = True
            for tag in self.tags:
                if tag not in product.tags:
                    hit = False
                    break

            if hit:
                result.append(product)

        return result
