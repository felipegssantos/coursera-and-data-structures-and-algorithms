# Uses python3
from collections import deque
import sys


def optimal_sequence(n):
    def next_candidates(k):
        candidates = list({k + 1, 2 * k, 3 * k})
        return [c for c in candidates if c <= n]

    dist = {0: 0}
    candidates = [1]
    counts = 1
    while True:
        new_candidates = []
        for j in candidates:
            dist[j] = counts
            new_candidates.extend(next_candidates(j))
        if n in dist.keys():
            break
        candidates = list(set(new_candidates) - set(dist.keys()))
        counts += 1

    sequence = deque()
    while n > 0:
        sequence.appendleft(n)
        if n % 3 == 0 and dist.get(n//3) == dist[n] - 1:
            n = n // 3
        elif n % 2 == 0 and dist.get(n//2) == dist[n] - 1:
            n = n // 2
        elif dist.get(n-1) == dist[n] - 1:
            n = n - 1
        else:
            raise RuntimeError(f"Backward pass failed for n={n}.\n"
                               f"Current sequence: {sequence}")

    return sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
