import unittest

from chess.move import Move


class TestMove(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_move_creation(self):
        pieces = ["P", "N", "B", "R", "Q", "K"]
        for piece in pieces:
            move = Move("e2", "e4", piece)
            self.assertEqual(move.piece, piece)

    def test_valid_squares(self):
        valid_squares = ["a1", "h1", "a8", "h8", "e4"]
        for square in valid_squares:
            move = Move(square, "e4", "P")
            self.assertEqual(move.source_position, square)
            move = Move("e2", square, "P")
            self.assertEqual(move.destination_position, square)

    def test_invalid_squares(self):
        invalid_squares = ["i1", "a9", "j0", "z0", "b-1", "1a", "00", "aa"]
        for square in invalid_squares:
            with self.assertRaises(ValueError):
                Move(square, "e4", "P")
            with self.assertRaises(ValueError):
                Move("e2", square, "P")

    def test_invalid_piece_type(self):
        with self.assertRaises(ValueError):
            Move("e2", "e4", "X")

    def test_accessor_methods(self):
        move = Move("e2", "e4", "P")
        self.assertEqual(move.source_position, "e2")
        self.assertEqual(move.destination_position, "e4")
        self.assertEqual(move.piece, "P")

    def test_string_representation(self):
        move = Move("e2", "e4", "P")
        self.assertEqual(str(move), "Pe2e4")

    def test_equality(self):
        move_1 = Move("e2", "e4", "P")
        move_2 = Move("e2", "e4", "P")
        move_3 = Move("d2", "d4", "P")
        self.assertEqual(move_1, move_2)
        self.assertNotEqual(move_1, move_3)
