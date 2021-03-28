from unittest import TestCase
from unittest import main
from unittest.mock import patch
import io

from game import roll_for_first_hit


class TestRollForFirstHit(TestCase):
    @patch('random.randint', side_effect=[50, 20])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_for_first_hit_player_first(self, mock_output, mock_random_number):
        test_player = {'name': 'Tom'}
        test_foe = {'name': 'Senpai'}
        roll_for_first_hit(test_player, test_foe)
        game_print = mock_output.getvalue()
        expected = "\nTom has rolled a 50\nSenpai has rolled a 20\n\n" \
                   "Tom has the first move!\n\n"
        self.assertEqual(game_print, expected)

    @patch('random.randint', side_effect=[20, 50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_for_first_hit_foe_first(self, mock_output, mock_random_number):
        test_player = {'name': 'Kerry'}
        test_feo = {'name': 'Tom'}
        roll_for_first_hit(test_player, test_feo)
        game_print = mock_output.getvalue()
        expected = "\nKerry has rolled a 20\nTom has rolled a 50\n\n" \
                   "Tom has the first move!\n\n"
        self.assertEqual(game_print, expected)


if __name__ == "__main__":
    main()
