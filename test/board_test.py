import unittest

from chess.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def tearDown(self) -> None:
        self.board = None

    def test_initialise(self):
        pass

    def test_get_piece(self):
        pass

    def test_place_piece(self):
        pass

    def test_remove_piece(self):
        pass

    def test_print_state(self):
        pass
