import pytest
from chess.enums.board import File, Rank


class TestFile:
    def test_file(self):
        expected_files = ["A", "B", "C", "D", "E", "F", "G", "H"]
        assert all(file in File.__members__ for file in expected_files)
        assert len(File) == 8
        assert File.A.value == 1
        assert File.B.value == 2
        assert File.C.value == 3
        assert File.D.value == 4
        assert File.E.value == 5
        assert File.F.value == 6
        assert File.G.value == 7
        assert File.H.value == 8


class TestRank:
    def test_rank(self):
        expected_ranks = [
            "ONE",
            "TWO",
            "THREE",
            "FOUR",
            "FIVE",
            "SIX",
            "SEVEN",
            "EIGHT",
        ]
        assert all(rank in Rank.__members__ for rank in expected_ranks)
        assert len(Rank) == 8

        assert Rank.ONE.value == 1
        assert Rank.TWO.value == 2
        assert Rank.THREE.value == 3
        assert Rank.FOUR.value == 4
        assert Rank.FIVE.value == 5
        assert Rank.SIX.value == 6
        assert Rank.SEVEN.value == 7
        assert Rank.EIGHT.value == 8


class TestSquare:
    def test_square_creation(self):
        pass

    def test_square_representation(self):
        pass

    def test_square_equality(self):
        pass

    def test_square_from_string(self):
        pass

    def test_invalid_square_from_string(self):
        pass

    def test_all_squares(self):
        pass

    def test_square_file_rank_values(self):
        pass
