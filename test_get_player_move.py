import io
from unittest import TestCase
from unittest.mock import patch

from game import get_player_move


class TestGetPlayerMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0"])
    def test_class_choice_return_string(self, mock_input, mock_output):
        actual = get_player_move()
        expected = str
        self.assertEqual(type(actual), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0", "1", "2", "3", "q", "Q", "h", "H"])
    def test_class_choice_return_correct_output(self, mock_input, mock_output):
        counter = 0
        expected = ["0", "1", "2", "3", "q", "Q", "h", "H"]
        for user_input in range(8):
            actual = get_player_move()
            self.assertEqual(actual, expected[counter])
            counter += 1

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["7", "0"])
    def test_class_choice_return_invalid_message(self, mock_input, mock_output):
        get_player_move()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "\nInstructions:" \
                          "\n \033[31m0\033[0m : Up " \
                          "\n \033[31m1\033[0m : Down " \
                          "\n \033[31m2\033[0m : Left" \
                          "\n \033[31m3\033[0m : Right" \
                          "\n \033[33mQ\033[0m : Quit" \
                          "\n\n\nInvalid Input\nPlease Try Again\n\n"
        self.assertEqual(expected_output, the_game_printed_this)
