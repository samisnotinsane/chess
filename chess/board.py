class Board:
    def __init__(self) -> None:
        self.empty = ""

        self.white_pawn = "P"
        self.black_pawn = "p"

        self.white_rook = "R"
        self.black_rook = "r"

        self.white_knight = "N"
        self.black_knight = "n"

        self.white_bishop = "B"
        self.black_bishop = "b"

        self.white_queen = "Q"
        self.black_queen = "q"

        self.white_king = "K"
        self.black_king = "k"

        self.initialise()
