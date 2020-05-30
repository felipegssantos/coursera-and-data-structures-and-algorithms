# Uses python3
import sys


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    pisano_period = get_pisano_period(m)
    smaller_fibonacci = calc_fib(n % pisano_period)
    return smaller_fibonacci % m


def get_pisano_period(m):
    seq = [0, 1]
    n = 2
    while True:
        seq.append(get_fibonacci_last_digit(n, m))
        seq.append(get_fibonacci_last_digit(n+1, m))
        candidate_period = len(seq) // 2
        if seq[:candidate_period] == seq[-candidate_period:]:
            return candidate_period
        else:
            n += 2


def get_fibonacci_last_digit(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current % m


def calc_fib(n):
    if n in [0, 1]:
        return n
    else:
        f1, f2 = 0, 1
        for _ in range(n-1):  # n-1 iterations because we start at n=2
            f1, f2 = f2, f1+f2
        return f2


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
