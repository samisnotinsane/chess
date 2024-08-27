from abc import ABC, abstractmethod
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.square import Square


class BaseValidator(ABC):
    """
    Base class for move validators.

    This abstract class defines the interface for piece-specific move validators.
    """

    @abstractmethod
    def generate_moves(self, board: BoardState, square: Square) -> list[Move]:
        """
        Generate all possible moves for a piece on a given square.

        Args:
            board (BoardState): The current board state.
            square (Square): The square containing the piece to generate moves for.

        Returns:
            list[Move]: A list of all possible moves for the piece.
        """
        pass
