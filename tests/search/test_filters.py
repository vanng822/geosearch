import unittest

from search import TagFilter, RadiusFilter

from models import Product


class RadiusFilterTest(unittest.TestCase):

    def setUp(self):
        # Rome
        self.lat = 41.8723889
        self.lng = 12.48018019999995
        self.items = [
            self._create_product(41.876748, 12.469616),
            self._create_product(41.878522, 12.489014),  # 1km
            self._create_product(41.863123, 12.500882)  # 2km
        ]

    def _create_product(self, lat, lng):
        return Product('567d07d533d541dd8ad4753622e76243',
                       '4aa53e646bf84faca9a76c020b0682de',
                       'testing and testing',
                       0.99,
                       0.66,
                       lng,
                       lat)

    def test_apply_1_km(self):
        # adding 1 meter extra to avoid floating point error
        f = RadiusFilter(self.lng, self.lat, 1001)
        result = f.apply(self.items)
        self.assertEqual(2, len(result))
        self.assertEqual(result[0].lng, 12.469616)
        self.assertEqual(result[1].lat, 41.878522)

    def test_apply_2_km(self):
        f = RadiusFilter(self.lng, self.lat, 2001)
        result = f.apply(self.items)
        self.assertEqual(3, len(result))
        self.assertEqual(result[0].lng, 12.469616)
        self.assertEqual(result[1].lat, 41.878522)
        self.assertEqual(result[2].lat, 41.863123)


class TagFilterTest(unittest.TestCase):

    def setUp(self):
        self.items = [Product('567d07d533d541dd8ad4753622e76243',
                              '4aa53e646bf84faca9a76c020b0682de',
                              'testing and testing',
                              0.99,
                              0.66,
                              18.06061237898499,
                              59.33265972650577,
                              tags=['hej', 'hopp']),
                      Product('567d07d533d541dd8ad4753622e76241',
                              '4aa53e646bf84faca9a76c020b0682de',
                              'testing and testing 2',
                              0.99,
                              0.66,
                              18.06061237898499,
                              59.33265972650577,
                              tags=['hej', 'mopp'])]

    def test_both_matched(self):
        f = TagFilter(['hej'])
        result = f.apply(self.items)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, '567d07d533d541dd8ad4753622e76243')
        self.assertEqual(result[1].id, '567d07d533d541dd8ad4753622e76241')

    def test_matched_hopp(self):
        f = TagFilter(['hopp'])
        result = f.apply(self.items)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, '567d07d533d541dd8ad4753622e76243')

    def test_matched_mopp(self):
        f = TagFilter(['mopp'])
        result = f.apply(self.items)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, '567d07d533d541dd8ad4753622e76241')
