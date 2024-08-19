class Move:
    valid_pieces: list[str] = ["P", "N", "B", "R", "Q", "K"]

    def __init__(self, src_pos: str, dest_pos: str, piece: str):
        if not self.is_valid_piece(piece):
            raise ValueError(f"Illegal piece '{piece}'")
        if not self.is_valid_position(src_pos):
            raise ValueError(f"Illegal start position '{src_pos}'")
        if not self.is_valid_position(dest_pos):
            raise ValueError(f"Illegal end position '{dest_pos}'")

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

    def _is_valid_row(self, row: int) -> bool:
        return 1 <= row <= 8

    def _is_valid_col(self, col: str) -> bool:
        legal_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for c in legal_columns:
            if c.upper() == col:
                return True
            if c.lower() == col:
                return True
        return False

    def is_valid_position(self, position: str) -> bool:
        col, row = position[0], position[1]
        is_valid_row = self._is_valid_row(int(row))
        is_valid_col = self._is_valid_col(col)
        return is_valid_col and is_valid_row

    @property
    def source_position(self) -> str:
        return self._source

    @property
    def destination_position(self) -> str:
        return self._destination

    @property
    def piece(self) -> str:
        return self._piece
