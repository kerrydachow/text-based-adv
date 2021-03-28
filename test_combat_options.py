from unittest import TestCase
from unittest.mock import patch
import io

from game import combat_options


class TestCombatOptions(TestCase):
    @patch('builtins.input', side_effect=["5", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_options_invalid_input(self, mock_output, mock_input):
        test_player = {"min_damage": 5,
                       "max_damage": 15,
                       "hit_rate": 1,
                       "HP": 15,
                       "location": [0, 0],
                       "name": "attacker",
                       "master_class": "Fighter"}
        combat_options(test_player)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "[31m1[0m : Power Punch\n" \
                          "[31m2[0m : Roundhouse Kick\n" \
                          "[31m3[0m : Body Slam\n" \
                          "[31m4[0m : Flee\n\n" \
                          "Invalid Input\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=["4", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_options_at_boss_location(self, mock_output, mock_input):  # when at boss Flee is not option
        test_player = {"min_damage": 5,
                       "max_damage": 15,
                       "hit_rate": 1,
                       "HP": 15,
                       "location": [24, 24],
                       "name": "attacker",
                       "master_class": "Fighter"}
        combat_options(test_player)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "[31m1[0m : Power Punch\n" \
                          "[31m2[0m : Roundhouse Kick\n" \
                          "[31m3[0m : Body Slam\n\n" \
                          "Invalid Input\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=["1"])
    def test_combat_options_return_is_string(self, mock_input):
        test_player = {"min_damage": 5,
                       "max_damage": 15,
                       "hit_rate": 1,
                       "HP": 15,
                       "location": [0, 0],
                       "name": "attacker",
                       "master_class": "Amazon"}
        actual = combat_options(test_player)
        self.assertTrue(type(actual) == str)
