"""
This module contains unit tests for the pawn movement in the chess engine.

It covers various scenarios of pawn movement, including initial moves,
captures, promotions and special rules like en passant.
"""

import pytest
from chess_engine.core.move_generation.move_generator import MoveGenerator
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.piece import Piece
from chess_engine.core.models.square import Square
from chess_engine.core.enums import PieceType, Colour


@pytest.fixture
def move_generator() -> MoveGenerator:
    """
    Fixture to create a MoveGenerator instance for tests.

    Returns:
        MoveGenerator: An instance of the MoveGenerator class.
    """
    return MoveGenerator()


@pytest.fixture
def board() -> BoardState:
    """
    Fixture to create a BoardState instance for tests.

    Returns:
        BoardState: An instance of the BoardState class.
    """
    return BoardState()


def test_pawn_initial_move(move_generator: MoveGenerator, board: BoardState):
    """
    Test the initial two-square move option for pawns.

    This test checks if a pawn on its starting square can move both one and two
    squares forward.
    """
    board.set_piece_at(Square(0, 1), Piece(Colour.WHITE, PieceType.PAWN))
    moves = move_generator.generate_legal_moves(board)
    assert len(moves) == 2
    assert any(move.to_square == Square(0, 2) for move in moves)
    assert any(move.to_square == Square(0, 3) for move in moves)


def test_pawn_blocked(move_generator: MoveGenerator, board: BoardState):
    """
    Test that a pawn cannot move when blocked by another piece.

    This test checks that no moves are generated for a pawn when there's
    a piece directly in front of it.
    """
    board.set_piece_at(Square(0, 1), Piece(Colour.WHITE, PieceType.PAWN))
    board.set_piece_at(Square(0, 2), Piece(Colour.BLACK, PieceType.PAWN))
    moves = move_generator.generate_legal_moves(board)
    assert len(moves) == 0


def test_pawn_capture(move_generator: MoveGenerator, board: BoardState):
    """
    Test pawn capture moves.

    This test verifies that a pawn can capture diagonally and still move
    forward when not blocked.
    """
    board.set_piece_at(Square(1, 1), Piece(Colour.WHITE, PieceType.PAWN))
    board.set_piece_at(Square(0, 2), Piece(Colour.WHITE, PieceType.PAWN))
    board.set_piece_at(Square(2, 2), Piece(Colour.BLACK, PieceType.PAWN))
    moves = move_generator.generate_legal_moves(board)
    assert len(moves) == 4
    assert any(move.to_square == Square(0, 2) for move in moves)
    assert any(move.to_square == Square(2, 2) for move in moves)


def test_pawn_en_passant(move_generator: MoveGenerator, board: BoardState):
    """
    Test en passant capture for pawns.

    Test test checks if a pawn can perform an en passant capture when the
    condition is met.
    """
    board.set_piece_at(Square(1, 4), Piece(Colour.WHITE, PieceType.PAWN))
    board.set_piece_at(Square(0, 4), Piece(Colour.BLACK, PieceType.PAWN))
    board._en_passant_square = Square(0, 5)
    moves = move_generator.generate_legal_moves(board)
    assert any(move.to_square == Square(0, 5) and move.is_en_passant for move in moves)
