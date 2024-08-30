from enum import Enum, auto


class Colour(Enum):
    """Represents the colour of a chess piece."""

    WHITE = auto()
    BLACK = auto()


class PieceType(Enum):
    """Represents the type of a chess piece."""

    PAWN = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROOK = auto()
    QUEEN = auto()
    KING = auto()


class MoveDirection(Enum):
    """
    Represents the direction of movement of a chess piece.

    For any PieceType:
        if Colour.WHITE then MoveDirection.UP
        if Colour.BLACK then MoveDirection.DOWN
    """

    UP = auto()
    DOWN = auto()
