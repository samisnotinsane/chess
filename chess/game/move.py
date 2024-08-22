from chess.enums.piece import PieceType
from chess.game.interface.board import Board, Move, Square


class SimpleMove(Move):
    def __init__(self, source: Square, destination: Square, piece: PieceType) -> None:
        self._source = source
        self._destination = destination
        self._piece = piece
        self._moved_piece_colour = None

    @property
    def source(self) -> Square:
        return self._source

    @property
    def destination(self) -> Square:
        return self._destination

    @property
    def piece(self) -> PieceType:
        return self._piece

    def execute(self, board: Board) -> None:
        piece_and_colour = board.remove_piece(self._source)
        if piece_and_colour is None:
            raise ValueError(f"No piece as source square {self._source}")
        self._moved_piece_colour = piece_and_colour[1]
        board.place_piece(self._destination, self._piece, self._moved_piece_colour)

    def undo(self, board: Board) -> None:
        if self._moved_piece_colour is None:
            raise ValueError("Move has not been executed yet")
        board.remove_piece(self._destination)
        board.place_piece(self._source, self._piece, self._moved_piece_colour)

    def __repr__(self) -> str:
        return f"SimpleMove({self._source} -> {self._destination}, {self._piece})"


class CaptureMove(Move):
    def __init__(
        self,
        source: Square,
        destination: Square,
        piece: PieceType,
        captured_piece: PieceType,
    ) -> None:
        self._source = source
        self._destination = destination
        self._piece = piece
        self.__captured_piece = captured_piece
        self.__captured_piece_colour = None

    @property
    def source(self) -> Square:
        return self._source

    @property
    def destination(self) -> Square:
        return self._destination

    @property
    def piece(self) -> PieceType:
        return self._piece

    def execute(self, board: Board) -> None:
        captured = board.remove_piece(self.destination)
        if captured is None:
            raise ValueError(
                f"No piece to capture at destination square {self.destination}"
            )
        self.__captured_piece_colour = captured[1]
        piece_and_colour = board.remove_piece(self.source)
        if piece_and_colour is None:
            raise ValueError(f"No piece at source square {self.source}")
        self._moved_piece_colour = piece_and_colour[1]
        board.place_piece(self.destination, self.piece, self._moved_piece_colour)

    def undo(self, board: Board) -> None:
        if self._moved_piece_colour is None:
            raise ValueError("CaptureMove has not been executed yet")
        board.remove_piece(self.destination)
        board.place_piece(self.source, self.piece, self._moved_piece_colour)
        if self.__captured_piece_colour is not None:
            board.place_piece(
                self.destination, self.__captured_piece, self.__captured_piece_colour
            )
        else:
            raise ValueError(
                "Captured piece colour is indeterminate, this means the capture move that just took place was invalid."
            )

    def __repr__(self) -> str:
        return f"CaptureMove({self.source} -> {self.destination}, {self.piece} captures {self.__captured_piece})"

    def get_captured_piece(self) -> PieceType:
        return self.__captured_piece
