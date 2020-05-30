import pytest

from different_summands import optimal_summands


@pytest.mark.parametrize('n, expected',
                         [(6, [1, 2, 3]),
                          (8, [1, 2, 5]),
                          (2, [2])])
def test_optimal_summands(n, expected):
    assert optimal_summands(n) == expected
