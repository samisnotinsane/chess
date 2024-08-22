from enum import Enum


class PieceType(Enum):
    PAWN = "P"
    BISHOP = "N"
    KNIGHT = "B"
    ROOK = "R"
    QUEEN = "Q"
    KING = "K"


PIECE_VALUES = {
    PieceType.PAWN: 1,
    PieceType.KNIGHT: 3,
    PieceType.BISHOP: 3,
    PieceType.ROOK: 5,
    PieceType.QUEEN: 9,
    PieceType.KING: 100,
}


class Colour(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"
