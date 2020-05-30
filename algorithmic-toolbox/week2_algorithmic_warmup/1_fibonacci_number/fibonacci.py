# Uses python3
def calc_fib(n):
    if n in [0, 1]:
        return n
    else:
        f1, f2 = 0, 1
        for _ in range(n-1):  # n-1 iterations because we start at n=2
            f1, f2 = f2, f1+f2
        return f2


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
