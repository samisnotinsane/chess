class Move:
    def __init__(self, source, destination, piece) -> None:
        self.source = source
        self.destination = destination
        self.piece = piece

    def execute(self, board):
        pass

    def undo(self, board):
        pass


class CaptureMove(Move):
    def __init__(self, source, destination, piece, captured_piece):
        super().__init__(source, destination, piece)
        self.captured_piece = captured_piece

    def execute(self, board):
        super().execute(board)
        board.remove_piece(self.destination, self.captured_piece)

    def undo(self, board):
        super().undo(board)
        board.place_piece(self.destination, self.captured_piece)
