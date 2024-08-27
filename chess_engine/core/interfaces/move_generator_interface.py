from abc import ABC, abstractmethod
from ..models.move import Move
from board.board_state import BoardState


class IMoveGenerator(ABC):
    """Interface for move generation."""

    @abstractmethod
    def generate_legal_moves(self, board: BoardState) -> list[Move]:
        """
        Generate all legal moves for the current position.

        Args:
            board (BoardState): The current board state.

        Returns:
            list[Move]: A list of all legal moves in the current position.
        """
        pass

    @abstractmethod
    def is_move_legal(self, board: BoardState, move: Move):
        """
        Check if a given move is legal in the current position.

        Args:
            board (BoardState): The current board state.
            move (Move): The move to check for legality.

        Returns:
            bool: True if the move is legal, False otherwise.
        """
        pass
