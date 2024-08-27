from dataclasses import dataclass
from .square import Square
from ..enums import PieceType


@dataclass(frozen=True)
class Move:
    from_square: Square
    to_square: Square
    promotion: PieceType | None = None
    is_castling: bool = False
    is_en_passant: bool = False
