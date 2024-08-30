from chess_engine.core.enums import PieceType
from chess_engine.core.interfaces.move_generator_interface import IMoveGenerator
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from chess_engine.core.move_generation.move_validators.pawn_validator import (
    PawnMoveValidator,
)


class MoveGenerator(IMoveGenerator):
    """
    Generates legal moves for a given chess position.

    This class uses piece-specific validators to generate moves and then filters
    them to ensure only legal moves are returned.
    """

    def __init__(self) -> None:
        """Initialise the MoveGenerator with piece-specific move validators."""
        self._validators = {
            PieceType.PAWN: PawnMoveValidator(),
            # TODO: Initialise other piece validators.
        }

    def generate_legal_moves(self, board: BoardState) -> list[Move]:
        """
        Generate all legal moves for the current position.

        Args:
            board (BoardState): The current board state.

        Returns:
            list[Move]: A list of all legal moves in the current position.
        """
        pass

    def is_move_legal(self, board: BoardState, move: Move):
        """
        Check if a given move is legal in the current position.

        This method should implement the logic to check for
        checks, pins and other factors that determine move legality.

        Args:
            board (BoardState): The current board state.
            move (Move): The move to check for legality.

        Returns:
            bool: True if the move is legal, False otherwise.
        """
        pass
