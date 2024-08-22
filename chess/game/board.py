from chess.enums.board import File, Rank


class Square:
    def __init__(self, file: File, rank: Rank) -> None:
        self.file = file
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.file.name}{self.rank.value}"

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Square):
            return NotImplemented
        return self.file == other.file and self.rank == other.rank

    @classmethod
    def from_string(cls, s: str):
        if len(s) != 2:
            raise ValueError("String must be 2 characters in length")
        file = File[s[0].upper()]
        rank = Rank(int(s[1]))
        return cls(file, rank)
