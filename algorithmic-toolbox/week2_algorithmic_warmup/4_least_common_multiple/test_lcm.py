import pytest

from lcm import lcm


@pytest.mark.parametrize('a, b, answer',
                         [(6, 8, 24),
                          (761457, 614573, 467970912861)])
def test_lcm(a, b, answer):
    assert lcm(a, b) == answer
