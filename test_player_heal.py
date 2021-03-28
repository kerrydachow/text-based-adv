from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import player_heal


class TestPlayerHeal(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_heal_correct_heal(self, mock_output):
        test_player = {'HP': 5, 'max_HP': 20}
        player_heal(test_player)
        game_print = mock_output.getvalue()
        expected = f"\nYou have recovered HP \nYour new HP is 9\n"
        self.assertEqual(game_print, expected)



if __name__ == "__main__":
    main()


