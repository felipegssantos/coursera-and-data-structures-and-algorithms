# Uses python3
import sys


def get_change(m):
    n = 0
    for coin in (10, 5, 1):
        n += m // coin
        m = m % coin
    return n


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
