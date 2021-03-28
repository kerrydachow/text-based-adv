from unittest import TestCase
from unittest import main

from game import player_sub_class


class TestPlayerSubClass(TestCase):
    def test_player_sub_class_return_correct_sub_class(self):
        counter = 1
        for times in range(3):
            test_player = {"level": counter, "master_class": "Sorcerer"}
            actual = player_sub_class(test_player)
            expected = ["Magician", "Wizard", "High Wizard"]
            self.assertEqual(actual, expected[counter - 1])
            counter += 1

    def test_player_sub_class_return_string(self):
        test_player = {"level": 1, "master_class": "Fighter"}
        actual = type(player_sub_class(test_player))
        expected = str
        self.assertEqual(actual, expected)

    def test_player_sub_class_level2(self):
        test_player = {"level": 2, "master_class": "Hidden Lord"}
        actual = player_sub_class(test_player)
        expected = "Lord"
        self.assertEqual(actual, expected)

    def test_player_sub_class_level3(self):
        test_player = {"level": 3, "master_class": "Fighter"}
        actual = player_sub_class(test_player)
        expected = "Sensei"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main()

