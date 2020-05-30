# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        i = (left + right) // 2
        if x < a[i]:
            right = i - 1
        elif x > a[i]:
            left = i + 1
        elif x == a[i]:
            return i
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def stress_test():
    from random import randint

    n = 10
    a = sorted(list({randint(50, 100) for _ in range(n)}))

    i = 0
    while True:
        x = randint(0, 150)
        naive = linear_search(a, x)
        divide_and_conquer = binary_search(a, x)
        if naive != divide_and_conquer:
            print(f'naive={naive}, divide_and_conquer={divide_and_conquer}'
                  f' for a={a} and x={x}')
            break
        else:
            i += 1
            print(i, end='\r', flush=True)


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
