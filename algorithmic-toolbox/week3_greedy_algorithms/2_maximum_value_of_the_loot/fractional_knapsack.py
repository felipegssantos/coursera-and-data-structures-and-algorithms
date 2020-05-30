# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    def fractional_value(wv):
        w, v = wv
        return v / w
    value = 0.
    sorted_items = sorted(zip(weights, values), key=fractional_value, reverse=True)
    for w, v in sorted_items:
        if w <= capacity:
            value += v
            capacity -= w
        else:
            value += v * capacity / w
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
