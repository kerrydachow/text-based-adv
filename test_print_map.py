from unittest import TestCase
from game import print_map
from unittest import mock
import io


class TestPrintMap(TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_player_lower_bound(self, mock_stdout):
        game_board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
                      (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2),
                      (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        player_dictionary = {"location": [0, 0]}
        print_map(5, game_board, player_dictionary)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "\033[05m😇\033[0m [ ][ ][ ][ ]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
