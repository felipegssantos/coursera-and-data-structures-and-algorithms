import pytest

from build_heap import build_heap


@pytest.mark.parametrize('index, n_swaps',
                         [('01', 3),
                          ('02', 0),
                          ('03', 100),
                          ('04', 99990)])
def test_build_heap(index, n_swaps):
    # Load test input
    with open(f'tests/{index}') as input_file:
        n = int(input_file.readline())
        data = list(map(int, input_file.readline().split()))
    assert len(data) == n

    # Swap in-place and test number of swaps
    swaps = build_heap(data)
    assert len(swaps) <= n_swaps

    # Verify min-heap property
    bad_edges = []
    i = 0
    while 2*i+2 < n:
        if data[i] > data[2*i+1]:
            bad_edges.append((i, 2*i+1))
        if data[i] > data[2*i+2]:
            bad_edges.append((i, 2*i+2))
        i += 1

    assert not bad_edges
