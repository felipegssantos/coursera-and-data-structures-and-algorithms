import pytest

from fibonacci import calc_fib


@pytest.mark.parametrize('n, fib', enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]))
def test_calc_fib(n, fib):
    assert calc_fib(n) == fib
