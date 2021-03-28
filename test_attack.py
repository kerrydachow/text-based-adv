import io
from unittest import TestCase
from unittest.mock import patch

from game import attack


class TestAttack(TestCase):
    @patch('random.randint', return_value=5)
    @patch('game.hit_or_miss', return_value=True)
    def test_attack_return_hp(self, mock_randint, mock_boolean):
        test_attacker = {"min_damage": 5,
                         "max_damage": 15,
                         "hit_rate": 1,
                         "HP": 15,
                         "name": "attacker",
                         "attack_move": "punch"}
        test_receiver = {"min_damage": 5,
                         "max_damage": 15,
                         "hit_rate": 80,
                         "HP": 15,
                         "name": "receiver",
                         "attack_move": "kick"}
        attack(test_attacker, test_receiver)
        actual = test_receiver["HP"]
        expected = 10
        self.assertEqual(expected, actual)
