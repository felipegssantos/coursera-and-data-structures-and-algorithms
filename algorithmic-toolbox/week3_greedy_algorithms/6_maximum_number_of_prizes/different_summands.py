# Uses python3
import sys


def optimal_summands(n):
    summands = []
    current_sum = 0
    candidate = 1
    while True:
        if n - current_sum >= candidate:
            summands.append(candidate)
            current_sum += candidate
            candidate += 1
        else:
            summands[-1] += n - current_sum
            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
