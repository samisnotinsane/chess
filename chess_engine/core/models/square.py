from dataclasses import dataclass


@dataclass(frozen=True)
class Square:
    """
    Represents a square on the chess board.

    Attributes:
        file (int): The file of the square (0-7 representing a-h).
        rank (int): The rank of the square (0-7 representing 1-8).
    """

    file: int  # 0-7 representing a-h
    rank: int  # 0-7 representing 1-8
