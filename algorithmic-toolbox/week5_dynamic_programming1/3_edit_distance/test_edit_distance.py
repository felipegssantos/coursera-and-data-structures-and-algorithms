import pytest

from edit_distance import edit_distance


@pytest.mark.parametrize('x, y, expected',
                         [('ab', 'ab', 0),
                          ('short', 'ports', 3),
                          ('editing', 'distance', 5)])
def test_edit_distance(x, y, expected):
    assert edit_distance(x, y) == expected
