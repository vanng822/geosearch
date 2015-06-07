import unittest

from models import Shop


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.shop = Shop('4aa53e646bf84faca9a76c020b0682de',
                         'Kitten store',
                         18.06061237898499,
                         59.33265972650577)

    def test_add_tags(self):
        self.assertListEqual([], self.shop.tags)

        self.shop.add_tag('hej')
        self.assertListEqual(['hej'], self.shop.tags)

        self.shop.add_tag('hopp')
        self.assertListEqual(['hej', 'hopp'], self.shop.tags)
