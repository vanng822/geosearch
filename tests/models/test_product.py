import unittest

from models import Product


class ProductTest(unittest.TestCase):

    def test_to_dict(self):
        product = Product('567d07d533d541dd8ad4753622e76243',
                          '4aa53e646bf84faca9a76c020b0682de',
                          'testing and testing',
                          0.99,
                          0.66,
                          18.06061237898499,
                          59.33265972650577)
        expected = {
            'id': '567d07d533d541dd8ad4753622e76243',
            'title': 'testing and testing',
            'popularity': 0.99,
            'quantity': 0.66,
            'shop': {
                'id': '4aa53e646bf84faca9a76c020b0682de',
                'lng': 18.06061237898499,
                'lat': 59.33265972650577,
            }
        }
        self.assertDictEqual(expected, product.to_dict())

    def test_tags(self):
        product = Product('567d07d533d541dd8ad4753622e76243',
                          '4aa53e646bf84faca9a76c020b0682de',
                          'testing and testing',
                          0.99,
                          0.66,
                          18.06061237898499,
                          59.33265972650577)
        self.assertListEqual([], product.tags)

        product = Product('567d07d533d541dd8ad4753622e76243',
                          '4aa53e646bf84faca9a76c020b0682de',
                          'testing and testing',
                          0.99,
                          0.66,
                          18.06061237898499,
                          59.33265972650577,
                          tags=['hej', 'hopp'])

        self.assertListEqual(['hej', 'hopp'], product.tags)
