import pytest
from chess.enums.piece import PIECE_VALUES, Colour, PieceType


class TestColour:
    def test_black_and_white(self):
        assert isinstance(Colour.WHITE, Colour)
        assert isinstance(Colour.BLACK, Colour)
        assert len(Colour) == 2


class TestPieceType:
    def test_piece_types(self):
        expected_pieces = ["PAWN", "KNIGHT", "BISHOP", "ROOK", "QUEEN", "KING"]
        assert all(piece in PieceType.__members__ for piece in expected_pieces)
        assert len(PieceType) == len(expected_pieces)

    def test_piece_type_uniqueness(self):
        piece_types = list(PieceType)
        assert len(piece_types) == len(set(piece_types))

    def test_piece_type_values(self):
        expected_values = ["P", "N", "B", "R", "Q", "K"]
        for piece_type, expected_value in zip(PieceType, expected_values):
            assert piece_type.value == expected_value


class TestPieceValue:
    def test_piece_values(self):
        expected_values = {
            PieceType.PAWN: 1,
            PieceType.KNIGHT: 3,
            PieceType.BISHOP: 3,
            PieceType.ROOK: 5,
            PieceType.QUEEN: 9,
            PieceType.KING: 100,
        }
        assert PIECE_VALUES == expected_values

    def test_all_piece_types_have_values(self):
        assert set(PieceType) == set(PIECE_VALUES.keys())

    @pytest.mark.parametrize(
        "piece_type,expected_value",
        [
            (PieceType.PAWN, 1),
            (PieceType.KNIGHT, 3),
            (PieceType.BISHOP, 3),
            (PieceType.ROOK, 5),
            (PieceType.QUEEN, 9),
            (PieceType.KING, 100),
        ],
    )
    def test_individual_piece_values(self, piece_type, expected_value):
        assert PIECE_VALUES[piece_type] == expected_value

    def test_knight_bishop_equality(self):
        assert PIECE_VALUES[PieceType.KNIGHT] == PIECE_VALUES[PieceType.BISHOP]

    def piece_value_ordering(self):
        assert PIECE_VALUES[PieceType.PAWN] < PIECE_VALUES[PieceType.KNIGHT]
        assert PIECE_VALUES[PieceType.KNIGHT] < PIECE_VALUES[PieceType.ROOK]
        assert PIECE_VALUES[PieceType.ROOK] < PIECE_VALUES[PieceType.QUEEN]
        assert PIECE_VALUES[PieceType.QUEEN] < PIECE_VALUES[PieceType.KING]
