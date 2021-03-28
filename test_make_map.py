from unittest import TestCase
from game import make_map


class TestMakeMap(TestCase):
    def test_make_map_lower_bound(self):
        expected = [(0, 0), (0, 1), (1, 0), (1, 1)]
        actual = make_map(2)
        self.assertEqual(expected, actual)

