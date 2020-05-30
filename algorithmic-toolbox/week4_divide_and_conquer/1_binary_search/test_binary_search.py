from binary_search import binary_search

import pytest


@pytest.mark.parametrize(('a, b, expected'),
                         [([1, 5, 8, 12, 13], [8, 1, 23, 1, 11],
                           [2, 0, -1, 0, -1]),
                          ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                           [0, 1, 2, 3, 4])])
def test_binary_search(a, b, expected):
    for x, e in zip(b, expected):
        assert binary_search(a, x) == e
