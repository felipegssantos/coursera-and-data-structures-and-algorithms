import pytest

from largest_number import largest_number


@pytest.mark.parametrize('a, expected',
                         [('21 2', '221'),
                          ('9 4 6 1 9', '99641'),
                          ('23 39 92', '923923')])
def test_largest_number(a, expected):
    assert largest_number(a.split()) == expected
