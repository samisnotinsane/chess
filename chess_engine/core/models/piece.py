from dataclasses import dataclass
from ..enums import Colour, PieceType


@dataclass(frozen=True)
class Piece:
    """
    Represents a chess piece.

    Attributes:
        colour (Colour): The colour of the piece.
        piece_type (PieceType): The type of the piece.
    """

    colour: Colour
    piece_type: PieceType
