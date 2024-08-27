from chess_engine.core.enums import PieceType
from chess_engine.core.interfaces.move_generator_interface import IMoveGenerator
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from move_generation.move_validators.base_validator import BaseValidator
from move_generation.move_validators.pawn_validator import PawnMoveValidator


class MoveGenerator(IMoveGenerator):
    def __init__(self) -> None:
        self._validators = {
            PieceType.PAWN: PawnMoveValidator(),
        }

    def generate_legal_moves(self, board: BoardState) -> list[Move]:
        pass

    def is_move_legal(self, board: BoardState, move: Move):
        pass
