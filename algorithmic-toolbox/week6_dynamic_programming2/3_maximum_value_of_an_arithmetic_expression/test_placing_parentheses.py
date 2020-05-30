import pytest

from placing_parentheses import get_maximum_value


@pytest.mark.parametrize('dataset, expected',
                         [('1+5', 6),
                          ('5-8+7*4-8+9', 200)])
def test_get_maximum_value(dataset, expected):
    assert get_maximum_value(dataset) == expected
