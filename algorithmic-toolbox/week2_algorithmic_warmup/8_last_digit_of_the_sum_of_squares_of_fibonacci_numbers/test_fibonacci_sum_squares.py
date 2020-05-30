import pytest


from fibonacci_sum_squares import fibonacci_sum_squares


@pytest.mark.parametrize('n,expected', [(7, 3), (73, 1), (1234567890, 0)])
def test_fibonacci_sum_squares(n, expected):
    assert fibonacci_sum_squares(n) == expected
