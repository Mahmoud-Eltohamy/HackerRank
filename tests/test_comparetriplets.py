import pytest
from src.comparetriplets import compareTriplets

@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3], [3, 2, 1], [0, 0]),
    ([1, 2, 3], [4, 5, 6], [0, 3]),
    ([1, 2, 3], [0, 0, 0], [3, 0]),
    ([5, 6, 7], [3, 6, 10], [1, 1])
])
def test_compareTriplets(a, b, expected):
    assert compareTriplets(a, b) == expected

