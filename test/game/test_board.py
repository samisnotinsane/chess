import pytest
from chess.game.board import Square
from chess.enums.board import File, Rank


class TestSquare:
    def test_square_creation(self):
        square = Square(File.E, Rank.FOUR)
        assert square.file == File.E
        assert square.rank == Rank.FOUR

    def test_square_representation(self):
        square = Square(File.A, Rank.ONE)
        assert str(square) == "A1"
        square = Square(File.H, Rank.EIGHT)
        assert str(square) == "H8"

    def test_square_equality(self):
        square1 = Square(File.C, Rank.THREE)
        square2 = Square(File.C, Rank.THREE)
        square3 = Square(File.D, Rank.THREE)
        assert square1 == square2
        assert square1 != square3

    def test_square_from_string(self):
        square = Square.from_string("e4")
        assert square.file == File.E
        assert square.rank == Rank.FOUR

    def test_invalid_square_from_string(self):
        with pytest.raises(ValueError):
            Square.from_string("e45")
        with pytest.raises(KeyError):
            Square.from_string("i4")

    def test_square_from_string_case_insensitive(self):
        square1 = Square.from_string("e4")
        square2 = Square.from_string("E4")
        assert square1 == square2
