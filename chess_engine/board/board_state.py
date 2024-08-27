from typing import Dict
from ..core.interfaces.board_interface import IBoardState
from ..core.models.piece import Piece
from ..core.models.square import Square
from ..core.enums import Colour, PieceType


class BoardState(IBoardState):
    """Implementation of the chess board state."""

    def __init__(self) -> None:
        """Initialise an empty chess board."""
        self._board: Dict[Square, Piece | None] = {
            Square(file, rank): None for rank in range(8) for file in range(8)
        }

    def _is_valid_square(self, square: Square) -> bool:
        return 0 <= square.file < 8 and 0 <= square.rank < 8

    def get_piece_at(self, square: Square) -> Piece | None:
        if not self._is_valid_square(square):
            raise ValueError(f"Invalid square: {square}")
        return self._board[square]

    def set_piece_at(self, square: Square, piece: Piece | None) -> None:
        if not self._is_valid_square(square):
            raise ValueError(f"Invalid square: {square}")
        self._board[square] = piece

    def is_square_occupied(self, square: Square) -> bool:
        return self._board[square] is not None

    def get_all_pieces(self) -> dict[Square, Piece]:
        return {
            square: piece for square, piece in self._board.items() if piece is not None
        }

    def clear_board(self) -> None:
        for square in self._board:
            self._board[square] = None

    def set_initial_position(self) -> None:
        for file in range(8):
            self.set_piece_at(Square(file, 1), Piece(Colour.WHITE, PieceType.PAWN))
            self.set_piece_at(Square(file, 6), Piece(Colour.BLACK, PieceType.PAWN))

        piece_order = [
            PieceType.ROOK,
            PieceType.KNIGHT,
            PieceType.BISHOP,
            PieceType.QUEEN,
            PieceType.KING,
            PieceType.BISHOP,
            PieceType.KNIGHT,
            PieceType.ROOK,
        ]

        for file, piece_type in enumerate(piece_order):
            self.set_piece_at(Square(file, 0), Piece(Colour.WHITE, piece_type))
            self.set_piece_at(Square(file, 7), Piece(Colour.BLACK, piece_type))

    def make_move(self, move: Move) -> None:
        """
        Apply a move to the board, updating the board state.

        Args:
            move (Move): The move to apply to the board.
        """
        pass

    def unmake_move(self, move: Move) -> None:
        """
        Undo a move on the board, reverting the board state.

        Args:
            move (Move): The move to undo.
        """
        pass

    def is_king_in_check(self, colour: Colour) -> bool:
        """
        Check if the king of the specified colour is in check.

        Args:
            colour (Colour): The colour of the king that could be in check.

        Returns:
            bool: True if the king is in check, False otherwise.
        """
        pass
