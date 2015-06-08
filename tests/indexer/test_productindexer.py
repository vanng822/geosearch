import unittest
from models import Product
from indexer import ProductIndexer


class ProductIndexerTest(unittest.TestCase):

    def setUp(self):
        # Rome
        self.lat = 41.8723889
        self.lng = 12.48018019999995
        self.items = [
            self._create_product(41.876748, 12.469616, '1'),
            self._create_product(41.878522, 12.489014, '2'),  # 1km
            self._create_product(41.863123, 12.500882, '3')  # 2km
        ]

        self.searcher = ProductIndexer(index_name="")
        for item in self.items:
            self.searcher.index_product(item)

    def _create_product(self, lat, lng, delta_id):
        p = Product('567d07d533d541dd8ad4753622e76243' + delta_id,
                    '4aa53e646bf84faca9a76c020b0682de',
                    'testing and testing',
                    0.99,
                    0.66,
                    lng,
                    lat)

        return p

    def test_find_500m(self):
        result = self.searcher.find(self.lng, self.lat, 500)
        self.assertEqual(len(result), 0)

    def test_find_1km(self):
        result = self.searcher.find(self.lng, self.lat, 1001)
        self.assertEqual(len(result), 2)

    def test_find_2km(self):
        result = self.searcher.find(self.lng, self.lat, 2001)
        self.assertEqual(len(result), 3)
