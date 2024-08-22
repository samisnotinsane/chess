from chess.game.move import Move, CaptureMove
from chess.game.board import Square
from chess.enums.board import File, Rank
from chess.enums.piece import PieceType


class MockBoard:
    def __init__(self) -> None:
        self._removed_pieces = []
        self._placed_pieces = []

    def remove_piece(self, square, piece):
        self._removed_pieces.append((square, piece))

    def place_piece(self, square, piece):
        self._placed_pieces.append((square, piece))


class TestMove:
    def test_move_creation(self):
        source = Square(File.E, Rank.TWO)
        destination = Square(File.E, Rank.FOUR)
        piece = PieceType.PAWN
        move = Move(source, destination, piece)
        assert move.source == source
        assert move.destination == destination
        assert move.piece == piece

    def test_move_execute(self):
        source = Square(File.E, Rank.TWO)
        destination = Square(File.E, Rank.FOUR)
        piece = PieceType.PAWN
        move = Move(source, destination, piece)
        board = MockBoard()
        move.execute(board)
        # TODO:: implement move.execute then assert post-condition

    def test_move_undo(self):
        source = Square(File.E, Rank.TWO)
        destination = Square(File.E, Rank.FOUR)
        piece = PieceType.PAWN
        move = Move(source, destination, piece)
        board = MockBoard()
        move.undo(board)
        # TODO: implement move.undo then assert post-condition


class TestCaptureMove:
    def test_capture_move_creation(self):
        source = Square(File.E, Rank.FOUR)
        destination = Square(File.D, Rank.FIVE)
        piece = PieceType.PAWN
        captured_piece = PieceType.PAWN
        move = CaptureMove(source, destination, piece, captured_piece)
        assert move.source == source
        assert move.destination == destination
        assert move.piece == piece
        assert move.captured_piece == captured_piece

    def test_capture_move_execute(self):
        source = Square(File.E, Rank.FOUR)
        destination = Square(File.D, Rank.FIVE)
        piece = PieceType.PAWN
        captured_piece = PieceType.PAWN
        move = CaptureMove(source, destination, piece, captured_piece)
        board = MockBoard()
        move.execute(board)
        assert board._removed_pieces == [(destination, captured_piece)]

    def test_capture_move_undo(self):
        source = Square(File.E, Rank.FOUR)
        destination = Square(File.D, Rank.FIVE)
        piece = PieceType.PAWN
        captured_piece = PieceType.PAWN
        move = CaptureMove(source, destination, piece, captured_piece)
        board = MockBoard()
        move.undo(board)
        assert board._placed_pieces == [(destination, captured_piece)]
