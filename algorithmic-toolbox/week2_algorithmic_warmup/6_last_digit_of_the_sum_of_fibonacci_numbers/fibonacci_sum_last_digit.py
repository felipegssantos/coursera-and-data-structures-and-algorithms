# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    # Because F_n % 10 has a Pisano period of 60, so must have
    # the sum of all F_k from k=0 to k=n
    return fibonacci_sum_naive(n % 60)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
