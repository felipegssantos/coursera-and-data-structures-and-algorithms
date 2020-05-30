import pytest

from fibonacci_sum_last_digit import fibonacci_sum


@pytest.mark.parametrize('n,expected', [(3, 4), (100, 5)])
def test_fibonacci_sum_last_digit(n, expected):
    assert fibonacci_sum(n) == expected
