# Uses python3
import sys


def get_change(m):
    dist = [0]
    for i in range(1, m+1):
        dist.append(forward_pass(i, dist))
    return dist[-1]


def forward_pass(m, dist):
    coins = [1, 3, 4]
    counts = [dist[m-c] + 1 for c in coins if m >= c]
    min_counts = min(counts)
    return min_counts


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
