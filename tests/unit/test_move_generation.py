import pytest
from chess_engine.core.move_generation.move_generator import MoveGenerator
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.move import Move
from chess_engine.core.models.square import Square
from chess_engine.core.enums import PieceType, Colour


@pytest.fixture
def move_generator() -> MoveGenerator
    return MoveGenerator()

@pytest.fixture
def board() -> BoardState:
    return BoardState()

def test_pawn_moves(move_generator: MoveGenerator, board: BoardState) -> None:
    board.set_piece_at(Square(0, 1), Piece(Colour.WHITE, PieceType.PAWN))
    moves = move_generator.generate_legal_moves(board)
    assert len(moves) == 2

