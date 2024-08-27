import pytest
from chess_engine.core.move_generation.move_generator import MoveGenerator
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.move import Move
from chess_engine.core.models.square import Square
from chess_engine.core.enums import PieceType, Colour


@pytest.fixture
def move_generator() -> MoveGenerator
    """Fixture to create a MoveGenerator instance for tests."""
    return MoveGenerator()

@pytest.fixture
def board() -> BoardState:
    """Fixture to create a BoardState instance for tests."""
    return BoardState()

def test_pawn_moves(move_generator: MoveGenerator, board: BoardState) -> None:
    """
    Test pawn move generation.

    This test checks if the correct number of moves are generated for a pawn
    in its initial position.
    """
    board.set_piece_at(Square(0, 1), Piece(Colour.WHITE, PieceType.PAWN))
    moves = move_generator.generate_legal_moves(board)
    assert len(moves) == 2

