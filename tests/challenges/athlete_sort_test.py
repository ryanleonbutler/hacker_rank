import pytest

from challenges.athlete_sort import athlete_sort

k = 1


athletes_input = [
    [5, 3],
    [10, 2, 5],
    [7, 1, 0],
    [9, 9, 9],
    [1, 23, 12],
    [6, 5, 9],
]

athletes_expected = [
    [7, 1, 0],
    [10, 2, 5],
    [6, 5, 9],
    [9, 9, 9],
    [1, 23, 12],
]


@pytest.mark.parametrize(
    "athletes, sort_column, expected",
    [
        (athletes_input, 1, athletes_expected),
    ],
)
def test_athlete(athletes, sort_column, expected):
    assert athlete_sort(athletes, sort_column) == expected
