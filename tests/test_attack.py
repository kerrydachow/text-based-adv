import io
from unittest import TestCase
from unittest.mock import patch

from game import attack


class TestAttack(TestCase):
    @patch('random.randint', return_value=5)
    @patch('game.hit_or_miss', return_value=True)
    def test_attack_receiver_return_hp(self, mock_randint, mock_boolean):
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

    @patch('random.randint', return_value=5)
    @patch('game.hit_or_miss', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_attacker_hit(self, mock_output, mock_randint, mock_boolean):
        test_attacker = {"min_damage": 4,
                         "max_damage": 15,
                         "hit_rate": 1,
                         "HP": 15,
                         "name": "attacker",
                         "attack_move": "punch"}
        test_receiver = {"min_damage": 4,
                         "max_damage": 15,
                         "hit_rate": 80,
                         "HP": 15,
                         "name": "receiver",
                         "attack_move": "kick"}
        attack(test_attacker, test_receiver)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "attacker used \033[31mpunch\033[0m!\n" \
                          "attacker dealt 5 damage! | receiver HP:10\n\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.hit_or_miss', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_attacker_miss(self, mock_output, mock_boolean):
        test_attacker = {"min_damage": 1,
                         "max_damage": 15,
                         "hit_rate": 1,
                         "HP": 15,
                         "name": "attacker",
                         "attack_move": "punch"}
        test_receiver = {"min_damage": 1,
                         "max_damage": 15,
                         "hit_rate": 80,
                         "HP": 15,
                         "name": "receiver",
                         "attack_move": "kick"}
        attack(test_attacker, test_receiver)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "attacker used \033[31mpunch\033[0m!\n" \
                          "attacker missed! | receiver HP:15\n\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', return_value=20)
    @patch('game.hit_or_miss', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_attacker_dead(self, mock_output, mock_randint, mock_boolean):
        test_attacker = {"min_damage": 5,
                         "max_damage": 20,
                         "hit_rate": 1,
                         "HP": 15,
                         "name": "attacker",
                         "attack_move": "punch"}
        test_receiver = {"min_damage": 1,
                         "max_damage": 15,
                         "hit_rate": 80,
                         "HP": 20,
                         "name": "receiver",
                         "attack_move": "kick"}
        attack(test_attacker, test_receiver)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "attacker used \033[31mpunch\033[0m!\n" \
                          "attacker dealt 20 damage! | receiver HP:0\n" \
                          "receiver has died.\n\n"
        self.assertEqual(expected_output, the_game_printed_this)

