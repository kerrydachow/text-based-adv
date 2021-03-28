from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import class_choice


class TestClassChoice(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0"])
    def test_class_choice_return_string(self, mock_input, mock_output):
        actual = class_choice()
        expected = str
        self.assertEqual(type(actual), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0", "1", "2", "3", "1337"])
    def test_class_choice_return_correct_class(self, mock_input, mock_output):
        counter = 0
        expected = ["Sorcerer", "Thief", "Amazon", "Fighter", "Hidden Lord"]
        for player_jobs in range(5):
            actual = class_choice()
            self.assertEqual(actual, expected[counter])
            counter += 1

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["7", "0"])
    def test_class_choice_return_invalid_message(self, mock_input, mock_output):
        class_choice()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "\nPlease input valid input\n\n"
        self.assertEqual(expected_output, the_game_printed_this)


if __name__ == "__main__":
    main()
