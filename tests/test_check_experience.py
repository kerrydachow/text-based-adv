from unittest import TestCase
from unittest import main

from game import check_experience


class TestCheckExperience(TestCase):
    def test_check_experience_level2(self):
        actual = check_experience({'XP': 20})
        self.assertTrue(actual)

    def test_check_experience_level3(self):
        actual = check_experience({'XP': 40})
        self.assertTrue(actual)

    def test_check_experience_no_levelup(self):
        actual = check_experience({'XP': 5})
        self.assertFalse(actual)


if __name__ == "__main__":
    main()
