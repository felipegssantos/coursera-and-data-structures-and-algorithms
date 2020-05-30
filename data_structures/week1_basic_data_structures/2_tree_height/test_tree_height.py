from pathlib import Path

import pytest

from tree_height import compute_height


def load_test_files():
    path = Path(__file__, '../tests').resolve()
    for i in range(1, 25):
        i_str = str(i).rjust(2, '0')
        with open(Path(path, i_str)) as input_file:
            n = int(input_file.readline().strip())
            nodes = list(map(int, input_file.readline().split()))
        with open(Path(path, f'{i_str}.a')) as answer_file:
            height = int(answer_file.readline())
        yield n, nodes, height


@pytest.mark.parametrize('n, nodes, height', list(load_test_files()))
def test_compute_height(n, nodes, height):
    assert compute_height(n, nodes) == height
