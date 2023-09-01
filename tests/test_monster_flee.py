from unittest import TestCase
from unittest import main
from unittest.mock import patch

from game import monster_flee


class TestMonsterFlee(TestCase):
    @patch('random.randint', return_value=5)
    def test_monster_flee_when_monster_flee(self, mock_random_number):
        actual = monster_flee({'location': [1, 1]})
        self.assertTrue(actual)

    def test_monster_flee_when_fight_boss(self):
        actual = monster_flee({'location': [24, 24]})
        self.assertFalse(actual)


if __name__ == "__main__":
    main()
