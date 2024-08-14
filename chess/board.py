class Board:
    def __init__(self) -> None:
        self.state = []
        self.empty = " "

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

        self.is_white_turn = True
        self.move_count = 0
        self.is_game_active = True
        self.last_move = None

    def initialise(self) -> None:
        # step 1: create a blank board
        for _ in range(8):
            row = []
            for _ in range(8):
                row.append(self.empty)
            self.state.append(row)

        # step 2: place the pawns on the second ranks
        for i in range(8):
            self.place(row=6, col=i, value=self.white_pawn)
            self.place(row=1, col=i, value=self.black_pawn)

        # step 3: place the rooks in the corners
        self.place(row=7, col=0, value=self.white_rook)
        self.place(row=7, col=7, value=self.white_rook)
        self.place(row=0, col=0, value=self.black_rook)
        self.place(row=0, col=7, value=self.black_rook)

        # step 4: place the knights next to the rooks
        self.place(row=7, col=1, value=self.white_knight)
        self.place(row=7, col=6, value=self.white_knight)
        self.place(row=0, col=1, value=self.black_knight)
        self.place(row=0, col=6, value=self.black_knight)

        # step 5: place the bishops next to knights
        self.place(row=7, col=2, value=self.white_bishop)
        self.place(row=7, col=5, value=self.white_bishop)
        self.place(row=0, col=2, value=self.black_bishop)
        self.place(row=0, col=5, value=self.black_bishop)

        # step 6: place the queen next to the left bishop
        self.place(row=7, col=3, value=self.white_queen)
        self.place(row=0, col=3, value=self.black_queen)

        # step 7: place the king next to the queen
        self.place(row=7, col=4, value=self.white_king)
        self.place(row=0, col=4, value=self.black_king)

    def print_state(self) -> None:
        for i in range(8):
            for j in range(8):
                val = self.state[i][j]
                if j == 7:
                    print(f"|{val}|")
                    break
                print(f"|{val}", end="")

    def place(self, row: int, col: int, value: str) -> None:
        self.state[row][col] = value

    def get(self, row: int, col: int) -> str:
        return self.state[row][col]

    def remove(self, row: int, col: int) -> None:
        self.state[row][col] = self.empty

    def move(self, start: tuple[int, int], end: tuple[int, int]):
        x1, y1 = start
        x2, y2 = end
        self.place(row=x2, col=y2, value=self.get(row=x1, col=y1))
        self.remove(row=x1, col=y1)
