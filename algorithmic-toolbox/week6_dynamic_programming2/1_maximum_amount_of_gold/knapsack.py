# Uses python3
import sys


def optimal_weight(W, w):
    values = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]
    for i in range(len(w)):
        for j in range(1, W+1):
            if j >= w[i] and values[i][j-w[i]] + w[i] > values[i][j]:
                values[i+1][j] = values[i][j-w[i]] + w[i]
            else:
                values[i+1][j] = values[i][j]
    return values[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
