import pytest

from primitive_calculator import optimal_sequence


@pytest.mark.parametrize('n, expected',
                         [(1, 1),
                          (5, 4),
                          (96234, 15)])
def test_optimal_sequence(n, expected):
    result = optimal_sequence(n)
    assert len(result) == expected
    assert result[-1] == n
    for i in range(1, len(result)):
        assert any((result[i] == result[i-1] + 1,
                    result[i] == 2 * result[i-1],
                    result[i] == 3 * result[i-1]))
