import pytest

from gcd import gcd


@pytest.mark.parametrize('a, b, divisor',
                         [(18, 35, 1),
                          (28851538, 1183019, 17657)])
def test_gcd(a, b, divisor):
    assert divisor == gcd(a, b)
