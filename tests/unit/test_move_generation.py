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


def test_pawn_initial_move(move_generator: MoveGenerator, board: BoardState) -> None:
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
