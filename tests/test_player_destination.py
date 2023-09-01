from unittest import TestCase
from unittest import main

from game import player_destination


class TestDetermineSubClass(TestCase):
    def test_player_destination_return_tuple(self):
        actual = type(player_destination("0", {'location': [0, 0]}))
        expected = tuple
        self.assertEqual(actual, expected)

    def test_player_destination_return_correct_up_location(self):
        actual = player_destination("0", {'location': [0, 0]})
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_player_destination_return_correct_down_location(self):
        actual = player_destination("1", {'location': [0, 1]})
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_player_destination_return_correct_left_location(self):
        actual = player_destination("2", {'location': [1, 0]})
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_player_destination_return_correct_right_location(self):
        actual = player_destination("3", {'location': [0, 0]})
        expected = (1, 0)
        self.assertEqual(actual, expected)

    def test_player_destination_negative_value(self):
        actual = player_destination("1", {'location': [0, 0]})
        expected = (0, -1)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main()
