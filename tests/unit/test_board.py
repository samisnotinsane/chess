import pytest
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.square import Square
from chess_engine.core.models.piece import Piece
from chess_engine.core.enums import Colour, PieceType


@pytest.fixture
def board():
    """Fixture to create a fresh BoardState for each test."""
    return BoardState()


def test_initial_position(board: BoardState):
    board.set_initial_position()
    assert board.get_piece_at(Square(0, 0)) == Piece(Colour.WHITE, PieceType.ROOK)
    assert board.get_piece_at(Square(4, 7)) == Piece(Colour.BLACK, PieceType.KING)
    assert board.get_piece_at(Square(3, 3)) is None


def test_set_and_get_piece(board: BoardState):
    piece = Piece(Colour.WHITE, PieceType.QUEEN)
    square = Square(3, 3)
    board.set_piece_at(square, piece)
    assert board.get_piece_at(square) == piece


def test_is_square_occupied(board: BoardState):
    square = Square(3, 3)
    assert not board.is_square_occupied(square)
    board.set_piece_at(square, Piece(Colour.WHITE, PieceType.PAWN))
    assert board.is_square_occupied(square)


def test_clear_board(board: BoardState):
    board.set_initial_position()
    board.clear_board()
    for file in range(8):
        for rank in range(8):
            assert board.get_piece_at(Square(file, rank)) is None


def test_get_all_pieces(board: BoardState):
    board.set_initial_position()
    pieces = board.get_all_pieces()
    assert len(pieces) == 32


def test_initial_position_specific_pieces(board: BoardState):
    board.set_initial_position()

    assert board.get_piece_at(Square(0, 0)) == Piece(Colour.WHITE, PieceType.ROOK)
    assert board.get_piece_at(Square(1, 0)) == Piece(Colour.WHITE, PieceType.KNIGHT)
    assert board.get_piece_at(Square(2, 0)) == Piece(Colour.WHITE, PieceType.BISHOP)
    assert board.get_piece_at(Square(3, 0)) == Piece(Colour.WHITE, PieceType.QUEEN)
    assert board.get_piece_at(Square(4, 0)) == Piece(Colour.WHITE, PieceType.KING)
    assert board.get_piece_at(Square(5, 0)) == Piece(Colour.WHITE, PieceType.BISHOP)
    assert board.get_piece_at(Square(6, 0)) == Piece(Colour.WHITE, PieceType.KNIGHT)
    assert board.get_piece_at(Square(7, 0)) == Piece(Colour.WHITE, PieceType.ROOK)

    assert board.get_piece_at(Square(0, 7)) == Piece(Colour.BLACK, PieceType.ROOK)
    assert board.get_piece_at(Square(1, 7)) == Piece(Colour.BLACK, PieceType.KNIGHT)
    assert board.get_piece_at(Square(2, 7)) == Piece(Colour.BLACK, PieceType.BISHOP)
    assert board.get_piece_at(Square(3, 7)) == Piece(Colour.BLACK, PieceType.QUEEN)
    assert board.get_piece_at(Square(4, 7)) == Piece(Colour.BLACK, PieceType.KING)
    assert board.get_piece_at(Square(5, 7)) == Piece(Colour.BLACK, PieceType.BISHOP)
    assert board.get_piece_at(Square(6, 7)) == Piece(Colour.BLACK, PieceType.KNIGHT)
    assert board.get_piece_at(Square(7, 7)) == Piece(Colour.BLACK, PieceType.ROOK)

    for file in range(8):
        assert board.get_piece_at(Square(file, 1)) == Piece(
            Colour.WHITE, PieceType.PAWN
        )
        assert board.get_piece_at(Square(file, 6)) == Piece(
            Colour.BLACK, PieceType.PAWN
        )


def test_set_piece_at_invalid_square(board: BoardState):
    with pytest.raises(ValueError):
        board.set_piece_at(Square(8, 8), Piece(Colour.WHITE, PieceType.PAWN))


def test_get_piece_at_invalid_square(board: BoardState):
    with pytest.raises(ValueError):
        board.get_piece_at(Square(-1, 0))
