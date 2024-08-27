from .base_validator import BaseValidator
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from chess_engine.core.models.square import Square


class PawnMoveValidator(BaseValidator):
    """Move validator for pawn pieces."""

    def generate_moves(self, board: BoardState, square: Square) -> list[Move]:
        """
        Generate all possible moves for a pawn on a given square.

        This method should implement the specific move generation logic
        for pawns, including:
        - forward moves
        - captures
        - en passant
        - promotions.

        Args:
            board (BoardState): The current board state.
            square (Square): The square containing the pawn.

        Returns:
            list[Move]: A list of all possible moves for the pawn.
        """
        pass
