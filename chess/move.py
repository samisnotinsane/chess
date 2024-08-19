class Move:
    valid_pieces: list[str] = ["P", "N", "B", "R", "Q", "K"]

    def __init__(self, src_pos: str, dest_pos: str, piece: str):
        if not self.is_valid_piece(piece):
            raise ValueError(
                f"Invalid piece '{piece}'. Can only be one of: {self.valid_pieces}"
            )

        self._source: str = src_pos
        self._destination: str = dest_pos
        self._piece: str = piece

    def __eq__(self, other) -> bool:
        if isinstance(other, Move):
            return (
                self._source == other._source
                and self._destination == other._destination
                and self._piece == other._piece
            )
        return False

    def __repr__(self) -> str:
        return f"{self.piece}{self._source}{self._destination}"

    def move_to_str(self) -> str:
        return f"{self._piece}{self._source}{self._destination}"

    def is_valid_piece(self, piece: str) -> bool:
        return piece.upper() in self.valid_pieces

    def is_valid_position(self, position: str) -> bool:
        if len(position) != 2:
            return False
        col, row = position[0], position[1]
        if col.lower() not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            return False
        if row not in list(range(1, 9)):
            return False
        return True

    @property
    def source_position(self) -> str:
        return self._source

    @property
    def destination_position(self) -> str:
        return self._destination

    @property
    def piece(self) -> str:
        return self._piece
