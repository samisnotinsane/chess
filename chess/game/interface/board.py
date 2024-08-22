from abc import ABC, abstractmethod
from chess.enums.piece import PieceType, PieceColour
from chess.enums.board import File, Rank


class Square(ABC):
    @property
    @abstractmethod
    def file(self) -> File:
        """Get the file of the square."""
        pass

    @property
    @abstractmethod
    def rank(self) -> Rank:
        """Get the rank of the square."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the square (e.g. 'E4')."""
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Check if this square is equal to another square."""
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """Return a hash value for the square."""
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, s: str) -> "Square":
        """Create a Square object from a string representation (e.g. 'E4')."""
        pass

    @abstractmethod
    def to_index(self) -> int:
        """Convert the square to a 0-63 index (A1 = 0, H8 = 63)."""
        pass

    @classmethod
    @abstractmethod
    def from_index(cls, index: int) -> "Square":
        """Create a Square object from a 0-63 index."""
        pass

    @abstractmethod
    def is_light(self) -> bool:
        """Check if the square is light-coloured."""

    @abstractmethod
    def is_dark(self) -> bool:
        """Check if the square is dark-coloured."""
        pass


class Board(ABC):
    @abstractmethod
    def place_piece(
        self, square: Square, piece: PieceType, colour: PieceColour
    ) -> None:
        """Place a piece on the board at the specified square."""
        pass

    @abstractmethod
    def remove_piece(self, square: Square) -> tuple[PieceType, PieceColour] | None:
        """Remove and return the piece at the specified square, or None
        if the square is empty."""
        pass

    @abstractmethod
    def get_piece(self, square: Square) -> tuple[PieceType, PieceColour] | None:
        """Return the piece at the specified square, or None if the square is empty."""
        pass

    @abstractmethod
    def move_piece(self, source: Square, destination: Square) -> None:
        """Move a piece from one square to another."""
        pass

    @abstractmethod
    def is_square_occupied(self, square: Square) -> bool:
        """Check if a square is occupied by a piece."""
        pass

    @abstractmethod
    def get_all_pieces(self) -> dict[Square, tuple[PieceType, PieceColour]]:
        """Return a dictionary of all pieces on the board, with squares as keys."""
        pass

    @abstractmethod
    def clear_board(self) -> None:
        """Remove all pieces from the board."""
        pass

    @abstractmethod
    def set_from_fen(self, fen: str) -> None:
        """Set up the board from a FEN (Forsyth-Edwards Notation) string."""
        pass

    @abstractmethod
    def get_fen(self) -> str:
        """Return the current board state as a FEN (Forsyth-Edwards Notation) string."""
        pass


class Move(ABC):
    @property
    @abstractmethod
    def source(self) -> Square:
        """Get the source square of the move."""
        pass

    @property
    @abstractmethod
    def destination(self) -> Square:
        """Get the destination square of the move."""
        pass

    @property
    @abstractmethod
    def piece(self) -> PieceType:
        """Get the type of the piece being moved."""
        pass

    @abstractmethod
    def execute(self, board: Board) -> None:
        """
        Execute the move on the given board.

        :param board: The game board on which to execute the move.
        :raises ValueError: If the move cannot be executed.
        """
        pass

    @abstractmethod
    def undo(self, board: Board) -> None:
        """
        Undo the move on the given board.

        :param board: The game board on which to undo the move.
        :raises ValueError: If the move cannot be undone.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the move."""
        pass
