from chess.enums.board import File, Rank
from chess.enums.piece import PieceColour, PieceType
from chess.game.interface.board import Board, Square


class GameSquare(Square):
    def __init__(self, file: File, rank: Rank) -> None:
        self.__file = file
        self.__rank = rank

    @property
    def file(self) -> File:
        return self.__file

    @property
    def rank(self) -> Rank:
        return self.__rank

    def __repr__(self) -> str:
        return f"{self.file.name}{self.rank.value}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GameSquare):
            return NotImplemented
        return self.file == other.file and self.rank == other.rank

    def __hash__(self) -> int:
        return hash((self.file, self.rank))

    @classmethod
    def from_string(cls, s: str) -> "Square":
        if len(s) != 2:
            raise ValueError("String must be 2 characters in length")
        if s[0] > "h":
            raise ValueError("File out of bounds")
        if int(s[1]) > 8:
            raise ValueError("Rank out of bounds")
        file = File[s[0].upper()]
        rank = Rank(int(s[1]))
        return cls(file, rank)

    def to_index(self) -> int:
        return (self.rank.value - 1) * 8 + (self.file.value - 1)

    @classmethod
    def from_index(cls, index: int) -> "Square":
        if not 0 <= index < 64:
            raise ValueError("Index must be between 0 and 63")
        rank = Rank(index // 8 + 1)
        file = File(index % 8 + 1)
        return cls(file, rank)

    def is_dark(self) -> bool:
        return (self.file.value + self.rank.value) % 2 == 0

    def is_light(self) -> bool:
        return not self.is_dark()


class GameBoard(Board):
    def __init__(self) -> None:
        self._pieces = {}

    def place_piece(self, square: Square, piece: PieceType, colour: PieceColour):
        self._pieces[square] = (piece, colour)

    def remove_piece(self, square: Square) -> tuple[PieceType, PieceColour] | None:
        return self._pieces.pop(square, None)

    def get_piece(self, square: Square) -> tuple[PieceType, PieceColour] | None:
        return self._pieces.get(square)

    def move_piece(self, source: Square, destination: Square) -> None:
        piece = self.remove_piece(source)
        if piece:
            piece_type, piece_colour = piece
            self.place_piece(destination, piece_type, piece_colour)

    def is_square_occupied(self, square: Square) -> bool:
        return square in self._pieces

    def get_all_pieces(self) -> dict[Square, tuple[PieceType, PieceColour]]:
        return self._pieces.copy()

    def clear_board(self) -> None:
        self._pieces.clear()

    def set_from_fen(self, fen: str) -> None:
        raise NotImplementedError("This feature is not supported yet")

    def get_fen(self) -> str:
        raise NotImplementedError("This feature is not supported yet")
