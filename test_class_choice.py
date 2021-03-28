from unittest import TestCase
from unittest.mock import patch
import io

from game import class_choice


class TestClassChoice(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0"])
    def test_class_choice_return_string(self, mock_input, mock_output):
        class_choice()
        expected = str
        self.assertEquals(type(mock_output), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["0"])
    def test_class_choice_return_correct_class(self, mock_input, mock_output):
        class_choice()
        expected = "Sorcerer"
        self.assertEqual(mock_output, expected)
