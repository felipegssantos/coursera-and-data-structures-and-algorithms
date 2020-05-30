from sorting import randomized_quick_sort, partition2, partition3

import pytest


@pytest.mark.parametrize('a, expected',
                         [([2, 3, 9, 2, 2], [2, 2, 2, 3, 9])])
def test_sorting(a, expected):
    randomized_quick_sort(a, 0, len(a) - 1)
    assert a == expected
