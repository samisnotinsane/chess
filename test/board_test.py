import sys
import unittest
from io import StringIO

from chess.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board: Board = Board()
        self.board.initialise()

    def tearDown(self) -> None:
        pass

    def test_initialise(self):
        # verify dimensions
        self.assertEqual(8, len(self.board.state))
        self.assertEqual(8, len(self.board.state[0]))

        # verify positions of pawns
        for i in range(8):
            self.assertEqual(self.board.get(6, i), self.board.white_pawn)
            self.assertEqual(self.board.get(1, i), self.board.black_pawn)

        # verify positions of rooks
        for i in [0, 7]:
            self.assertEqual(self.board.get(7, i), self.board.white_rook)
            self.assertEqual(self.board.get(0, i), self.board.black_rook)

        # verify positions of knights
        for i in [1, 6]:
            self.assertEqual(self.board.get(7, i), self.board.white_knight)
            self.assertEqual(self.board.get(0, i), self.board.black_knight)

        # verify positions of bishops
        for i in [2, 5]:
            self.assertEqual(self.board.get(7, i), self.board.white_bishop)
            self.assertEqual(self.board.get(0, i), self.board.black_bishop)

        # verify position of queen
        self.assertEqual(self.board.get(7, 3), self.board.white_queen)
        self.assertEqual(self.board.get(0, 3), self.board.black_queen)

        # verify position of king
        self.assertEqual(self.board.get(7, 4), self.board.white_king)
        self.assertEqual(self.board.get(0, 4), self.board.black_king)

    def test_get_piece(self):
        self.assertEqual(self.board.get(2, 0), self.board.empty)
        self.assertEqual(self.board.get(7, 4), self.board.white_king)
        self.assertEqual(self.board.get(0, 4), self.board.black_king)

    def test_place_piece(self):
        self.board.place(4, 4, self.board.white_queen)
        self.assertEqual(self.board.get(4, 4), self.board.white_queen)

    def test_remove_piece(self):
        self.board.remove(6, 0)
        self.assertEqual(self.board.get(6, 0), self.board.empty)

    def test_print_state(self):
        expected_output = (
            "|r|n|b|q|k|b|n|r|\n"
            "|p|p|p|p|p|p|p|p|\n"
            "| | | | | | | | |\n"
            "| | | | | | | | |\n"
            "| | | | | | | | |\n"
            "| | | | | | | | |\n"
            "|P|P|P|P|P|P|P|P|\n"
            "|R|N|B|Q|K|B|N|R|\n"
        )

        # redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output
        self.board.print_state()

        # reset redirect
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)
