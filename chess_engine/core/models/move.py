from dataclasses import dataclass
from .square import Square
from ..enums import PieceType


@dataclass(frozen=True)
class Move:
    """
    Represents a chess move.

    Attributes:
        from_square (Square): The starting square of the move.
        to_square (Square): The destination square of the move.
        promotion (PieceType | None): the piece type to promote to, if this is a promotion move.
        is_castling (bool): True if this move is a castling move.
        is_en_passant (bool): True if this move is an en passant capture.
    """

    from_square: Square
    to_square: Square
    promotion: PieceType | None = None
    is_castling: bool = False
    is_en_passant: bool = False
