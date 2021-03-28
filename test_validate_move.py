from unittest import TestCase
from unittest import main

from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_return_bool(self):
        board = [(2, 2), (1, 2), (0, 2), (2, 1), (1, 1), (0, 1), (2, 0), (1, 0), (0, 0)]
        test_location = (2, 0)
        actual = type(validate_move(test_location, board))
        expected = bool
        self.assertEqual(actual, expected)

    def test_validate_move_correct_return(self):
        board = [(2, 2), (1, 2), (0, 2), (2, 1), (1, 1), (0, 1), (2, 0), (1, 0), (0, 0)]
        test_location = (2, 2)
        actual = validate_move(test_location, board)
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main()
