from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import determine_sub_class


class TestDetermineSubClass(TestCase):
    def test_determine_sub_class_correct_subclass(self):
        game_class = ["Sorcerer", "Thief", "Amazon", "Fighter", "Hidden Lord"]
        expected = [["Magician", "Wizard", "High Wizard"], ["Thief", "Bandit", "Night Lord"], ["Novice", "Amazon", "Pathfinder"], ["Brawler", "Buccaneer", "Sensei"], ["Master", "Lord", "God"]]
        counter = 0
        for jobs in game_class:
            player = {"master_class": game_class[counter]}
            actual = determine_sub_class(player)
            self.assertEqual(actual, expected[counter])

    def test_determine_sub_class_correct_type(self):
        actual = determine_sub_class({"master_class": "Sorcerer"})
        expected = list
        self.assertEqual(type(actual), expected)

    def test_determine_sub_class_correct_length(self):
        actual = len(determine_sub_class({"master_class": "Hidden Lord"}))
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main()

