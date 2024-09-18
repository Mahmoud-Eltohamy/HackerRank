import pytest
from src.diagonalDifference import diagonalDifference


def test_diagonalDifference():
    assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15
    assert diagonalDifference([[1, 2, 3], [3, 2, 1], [1, 2, 3]]) == 0
    assert diagonalDifference([[5, 6, 7], [3, 6, 10], [10, 8, 5]]) == 7
