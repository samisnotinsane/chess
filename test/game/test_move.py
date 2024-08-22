import pytest
from chess.game.move import SimpleMove, CaptureMove
from chess.game.board import GameBoard, GameSquare
from chess.enums.board import File, Rank
from chess.enums.piece import PieceType, PieceColour


class TestMove:
    # TODO: Refactor test class to cover SimpleMove and CaptureMove.
    @pytest.fixture
    def board(self):
        return GameBoard()

    @pytest.fixture
    def simple_move(self):
        return SimpleMove(
            GameSquare(File.E, Rank.TWO), GameSquare(File.E, Rank.FOUR), PieceType.PAWN
        )

    def test_move_creation(self, simple_move):
        assert simple_move.source == GameSquare(File.E, Rank.TWO)
        assert simple_move.destination == GameSquare(File.E, Rank.FOUR)
        assert simple_move.piece == PieceType.PAWN

    def test_move_execute(self, board, simple_move):
        board.place_piece(simple_move.source, simple_move.piece, PieceColour.WHITE)
        simple_move.execute(board)
        assert board.get_piece(simple_move.source) is None
        assert board.get_piece(simple_move.destination) == (
            PieceType.PAWN,
            PieceColour.WHITE,
        )

    def test_move_undo(self, board, simple_move):
        board.place_piece(simple_move.destination, simple_move.piece, PieceColour.WHITE)
        simple_move.undo(board)
        assert board.get_piece(simple_move.destination) is None
        assert board.get_piece(simple_move.source) == (
            PieceType.PAWN,
            PieceColour.WHITE,
        )


class TestCaptureMove:
    @pytest.fixture
    def board(self):
        return GameBoard()

    @pytest.fixture
    def capture_move(self):
        return CaptureMove(
            GameSquare(File.E, Rank.FOUR),
            GameSquare(File.D, Rank.FIVE),
            PieceType.PAWN,
            PieceType.PAWN,
        )

    def test_capture_move_creation(self, capture_move):
        assert capture_move.source == GameSquare(File.E, Rank.FOUR)
        assert capture_move.destination == GameSquare(File.D, Rank.FIVE)
        assert capture_move.piece == PieceType.PAWN
        assert capture_move.get_captured_piece() == PieceType.PAWN

    def test_capture_move_execute(self, board, capture_move):
        board.place_piece(capture_move.source, capture_move.piece, PieceColour.WHITE)
        board.place_piece(
            capture_move.destination, capture_move.captured_piece, PieceColour.BLACK
        )
        capture_move.execute(board)
        assert board.get_piece(capture_move.source) is None
        assert board.get_piece(capture_move.destination) == (
            PieceType.PAWN,
            PieceColour.WHITE,
        )

    def test_capture_move_undo(self, board, capture_move):
        board.place_piece(
            capture_move.destination, capture_move.piece, PieceColour.WHITE
        )
        capture_move.undo(board)
        assert board.get_piece(capture_move.destination) == (
            capture_move.get_captured_piece(),
            PieceColour.BLACK,
        )
        assert board.get_piece(capture_move.source) == (
            capture_move.piece,
            PieceColour.WHITE,
        )
