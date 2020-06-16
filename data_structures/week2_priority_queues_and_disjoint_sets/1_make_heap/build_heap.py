# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)
    for i in reversed(range(n//2)):
        current = i
        left = 2 * current + 1
        right = left + 1
        # sift down until heap property is satisfied
        children = [c for c in [left, right] if c < n]
        while any([data[current] > data[c] for c in children]):
            if len(children) == 1:
                smallest = children[0]
            elif data[left] < data[right]:
                smallest = left
            else:
                smallest = right
            swaps.append((current, smallest))
            data[current], data[smallest] = data[smallest], data[current]
            current = smallest
            left = 2 * current + 1
            right = left + 1
            children = [c for c in [left, right] if c < n]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


def stress_test():
    from random import randint, shuffle
    j = 0
    while True:
        # n = randint(1, int(1e5))
        n = randint(1, 15)
        data = list(range(n))
        shuffle(data)
        raw = data.copy()
        swaps = build_heap(data)
        # Verify heap-property
        bad_edges = []
        i = 0
        while 2*i+2 < n:
            if data[i] > data[2*i+1]:
                bad_edges.append((i, 2*i+1))
            if data[i] > data[2*i+2]:
                bad_edges.append((i, 2*i+2))
            i += 1
        if bad_edges:
            print(f'Not a heap: raw={raw}, tree={data}')
            print(f'bad edges: {bad_edges}')
            break
        # Verify number of swaps
        if len(swaps) > 4 * n:
            print(f'Too many swaps - m={len(swaps)}, n={n}')
            break
        j += 1
        print(j, flush=True, end='\r')


if __name__ == "__main__":
    main()
    # stress_test()
