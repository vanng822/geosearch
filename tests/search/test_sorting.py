import unittest

from search import sort_by_popularity


class Dummy(object):

    def __init__(self, id, popularity):
        self.id = id
        self.popularity = popularity


class SortByPopularityTest(unittest.TestCase):

    def test_sort_by_popularity(self):
        d2 = Dummy(2, 14)
        d1 = Dummy(1, 10)
        d3 = Dummy(3, 5)

        expected = [d2, d1, d3]

        result = sort_by_popularity([d1, d2, d3])

        self.assertListEqual(expected, result)
