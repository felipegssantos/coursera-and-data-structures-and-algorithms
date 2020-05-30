import pytest

from fibonacci_last_digit import get_fibonacci_last_digit


@pytest.mark.parametrize('n, fib_last_digit',
                         [(327305, 5), (331, 9)] + list(enumerate([0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4])))
def test_calc_fib(n, fib_last_digit):
    assert get_fibonacci_last_digit(n) == fib_last_digit
