# Uses python3
import sys


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    a, b = sorted([a, b])
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
