from chess_engine.core.enums import PieceType
from chess_engine.core.interfaces.move_generator_interface import IMoveGenerator
from chess_engine.core.models.move import Move
from chess_engine.board.board_state import BoardState
from chess_engine.core.move_generation.move_validators.base_validator import (
    BaseValidator,
)
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
        self._validators: dict[PieceType, BaseValidator] = {
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
        all_moves = []
        for square, piece in board.get_all_pieces().items():
            validator = self._validators.get(piece.piece_type)
            if validator is None:
                raise ValueError(
                    f"No validator defined for piece {piece} in square {square}"
                )
            all_moves.extend(validator.generate_moves(board, square))
        return [move for move in all_moves if self.is_move_legal(board, move)]

    def is_move_legal(self, board: BoardState, move: Move) -> bool:
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
        if not board._is_valid_square(move.from_square) or not board._is_valid_square(
            move.to_square
        ):
            return False

        piece = board.get_piece_at(move.from_square)
        if piece is None:
            return False

        temp_board = board.copy()
        temp_board.make_move(move)

        if temp_board.is_king_in_check(piece.colour):
            return False

        # TODO: Add additional checks for:
        # - castling through check
        # - en passant

        return True
