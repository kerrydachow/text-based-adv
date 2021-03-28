from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import check_for_monster


class TestCheckForMonster(TestCase):
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=5)
    def test_check_for_monster_return_true(self, mock_random_number, mock_output):
        actual = check_for_monster({'location': [1, 1]})
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=50)
    def test_check_for_monster_return_false(self, mock_random_number):
        actual = check_for_monster({'location': [2, 2]})
        self.assertFalse(actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=5)
    def test_check_for_monster_message(self, mock_random_number, mock_output):
        check_for_monster({'location': [49, 49]})
        game_print = mock_output.getvalue()
        expected = "\nA monster has appeared!\n"
        self.assertEqual(game_print, expected)


if __name__ == "__main__":
    main()

