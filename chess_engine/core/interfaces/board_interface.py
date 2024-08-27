from abc import ABC, abstractmethod
from ..models.piece import Piece
from ..models.square import Square


class IBoardState(ABC):
    """Interface for the chess board state."""

    @abstractmethod
    def get_piece_at(self, square: Square) -> Piece | None:
        """
        Get the piece at the given square.

        Args:
            square (Square): The square to check.

        Returns:
            Piece | None: The piece at the square, or None if the square is empty.
        """
        pass

    @abstractmethod
    def set_piece_at(self, square: Square, piece: Piece | None) -> None:
        """
        Set a piece at the given square.

        Args:
            square (Square): The square to set the piece on.
            piece (Piece | None): The piece to set, or None to clear the square.
        """
        pass

    @abstractmethod
    def is_square_occupied(self, square: Square) -> bool:
        """
        Check if a square is occupied.

        Args:
            square (Square): The square to check.

        Returns:
            bool: True if the square is occupied, False otherwise.
        """
        pass

    @abstractmethod
    def get_all_pieces(self) -> dict[Square, Piece]:
        """
        Get all pieces currently on the board.

        Returns:
            dict[Square, Piece]: A dictionary mapping occupied squares to pieces.
        """
        pass

    @abstractmethod
    def clear_board(self) -> None:
        """Clear all pieces from the board."""
        pass

    @abstractmethod
    def set_initial_position(self) -> None:
        """
        Set the board to the initial chess position.

        This method places all pieces in their standard starting positions:
        - Pawns on the second and seventh ranks
        - Rooks on a1, h1, a8, h8
        - Knights on b1, g1, b8, g8
        - Bishops on c1, f1, c8, f8
        - Queens on d1 and d8
        - Kings on e1 and e8
        """
        pass
