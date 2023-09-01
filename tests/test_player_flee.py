from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import player_flee


class TestPlayerFlee(TestCase):
    @patch('random.randint', side_effect=[5, 4])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_flee_success(self, mock_output, mock_random_number):
        player_flee({'HP': 10})
        game_print = mock_output.getvalue()
        expected = "You fled but took a stab to the back 4\n"
        self.assertEqual(game_print, expected)
        
    @patch('random.randint', return_value=50)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_flee_failure(self, mock_output, mock_random_number):
        player_flee({'HP': 1919})
        game_print = mock_output.getvalue()
        expected = "You fled successfully!\n"
        self.assertEqual(game_print, expected)


if __name__ == "__main__":
    main()

