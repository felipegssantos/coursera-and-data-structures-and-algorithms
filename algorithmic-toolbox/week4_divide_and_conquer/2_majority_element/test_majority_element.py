from majority_element import get_majority_element

import pytest


@pytest.mark.parametrize('seq, expected',
                         [([2, 3, 9, 2, 2], 2),
                          ([1, 2, 3, 4], -1),
                          ([1, 2, 3, 1], -1)])
def test_get_majority_element(seq, expected):
    assert get_majority_element(seq, 0, len(seq)) == expected
