from chess_engine.core.enums import Colour, MoveDirection
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
        moves = []
        pawn = board.get_piece_at(square)
        if pawn:
            direction = self._get_pawn_direction(pawn.colour)

            if self._is_on_starting_rank(square, pawn.colour):
                moves.extend(self._generate_forward_moves(board, square, direction))

        return moves

    def _get_pawn_direction(self, colour: Colour) -> MoveDirection:
        """
        Determine the direction in which the pawn moves based on its colour.

        Args:
            colour (Colour): The colour of the pawn.

        Returns:
            MoveDirection: The direction of movement, either:
                MoveDirection.UP for Colour.WHITE or
                MoveDirection.DOWN for Colour.BLACK
        """
        return MoveDirection.UP if colour == Colour.WHITE else MoveDirection.DOWN

    def _is_on_starting_rank(self, square: Square, colour: Colour) -> bool:
        """
        Check if the pawn is on its starting rank.

        Args:
            square (Square): The square containing the pawn.
            colour (Colour): The colour of the pawn.

        Returns: True if the pawn is on its starting rank, False otherwise.
        """
        return (colour == Colour.WHITE and square.rank == 1) or (
            colour == Colour.BLACK and square.rank == 6
        )

    def _generate_forward_moves(
        self, board: BoardState, square: Square, direction: MoveDirection
    ) -> list[Move]:
        """
        Generate forward moves for a pawn from its starting position.

        Args:
            board (BoardState): The current board state.
            square (Square): The square containing the pawn.
            direction (MoveDirection): The direction of the pawn moves.

        Returns:
            list[Move]: A list of possible forward moves.
        """
        moves = []
        move_direction = 0
        if direction == MoveDirection.UP:
            move_direction = 1
        if direction == MoveDirection.DOWN:
            move_direction = -1

        forward = Square(square.file, square.rank + move_direction)

        if not board.is_square_occupied(forward):
            moves.append(Move(square, forward))

            double_forward = Square(square.file, square.rank + (2 * move_direction))
            if not board.is_square_occupied(double_forward):
                moves.append(Move(square, double_forward))

        return moves
