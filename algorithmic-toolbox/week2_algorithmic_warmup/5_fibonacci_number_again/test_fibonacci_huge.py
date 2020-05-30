import pytest

from fibonacci_huge import get_fibonacci_huge, get_pisano_period


@pytest.mark.parametrize('n, m, out',
                         [(239, 1000, 161),
                          (2816213588, 239, 151),
                          (327305, 10, 5),
                          (331, 10, 9)])
def test_get_fibonacci_huge(n, m, out):
    assert get_fibonacci_huge(n, m) == out


@pytest.mark.parametrize('m, out',
                         [(2, 3),
                          (3, 8),
                          (4, 6),
                          (5, 20),
                          (6, 24),
                          (7, 16),
                          (8, 12),
                          (9, 24),
                          (10, 60),
                          (11, 10),
                          (12, 24)])
def test_get_pisano_period(m, out):
    assert get_pisano_period(m) == out
