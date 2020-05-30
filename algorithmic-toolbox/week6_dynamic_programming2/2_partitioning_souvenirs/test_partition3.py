import pytest

from partition3 import partition3


@pytest.mark.parametrize('A, expected',
                         [([3, 3, 3, 3], 0),
                          ([40], 0),
                          ([1, 3, 3, 2], 1),
                          ([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 1),
                          ([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 1),
                          ([2, 2, 8, 1, 6, 5, 9, 12], 1)])
def test_partition3(A, expected):
    assert partition3(A) == expected
