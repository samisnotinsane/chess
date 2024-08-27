from .base_validator import BaseValidator
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.square import Square


class PawnMoveValidator(BaseValidator):
    def generate_moves(self, board: BoardState, square: Square) -> list[Move]:
        pass
