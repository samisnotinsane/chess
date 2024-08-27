from abc import ABC, abstractmethod
from ..models.move import Move
from board.board_state import BoardState


class IMoveGenerator(ABC):
    @abstractmethod
    def generate_legal_moves(self, board: BoardState) -> list[Move]:
        pass

    @abstractmethod
    def is_move_legal(self, board: BoardState, move: Move):
        pass
