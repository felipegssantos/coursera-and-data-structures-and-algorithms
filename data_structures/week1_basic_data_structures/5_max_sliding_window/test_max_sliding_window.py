import pytest

from max_sliding_window import max_sliding_window


@pytest.mark.parametrize('sequence, window_size, sliding_max',
                         [([2, 7, 3, 1, 5, 2, 6, 2], 4, [7, 7, 5, 6, 6])])
def test_max_sliding_window(sequence, window_size, sliding_max):
    assert max_sliding_window(sequence, window_size) == sliding_max
