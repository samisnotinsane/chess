import unittest

from chess.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board: Board = Board()

    def tearDown(self) -> None:
        pass

    def test_initialise(self):
        self.board.initialise()
        print()
        self.board.print_state()

    @unittest.skip("Not yet implemented")
    def test_get_piece(self):
        pass

    @unittest.skip("Not yet implemented")
    def test_place_piece(self):
        pass

    @unittest.skip("Not yet implemented")
    def test_remove_piece(self):
        pass

    @unittest.skip("Not yet implemented")
    def test_print_state(self):
        pass
