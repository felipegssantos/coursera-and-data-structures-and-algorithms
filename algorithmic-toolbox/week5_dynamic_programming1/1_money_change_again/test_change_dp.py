import pytest

from change_dp import get_change


@pytest.mark.parametrize('m, expected',
                         [(2, 2), (34, 9)])
def test_change_dp(m, expected):
    assert get_change(m) == expected
