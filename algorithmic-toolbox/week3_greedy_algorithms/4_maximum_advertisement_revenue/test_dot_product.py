import pytest

from dot_product import max_dot_product


@pytest.mark.parametrize('a, b, expected',
                         [([23], [39], 897),
                          ([1, 3, -5], [-2, 4, 1], 23)])
def test_max_dot_product(a, b, expected):
    assert max_dot_product(a, b) == expected
