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


def fibonacci_partial_sum(from_, to):
    # F_m + ... + F_n = S_n - S_{m-1}
    # with S_k = F_0 + ... + F_k
    return (fibonacci_sum(to) - fibonacci_sum(from_ - 1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
