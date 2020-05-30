# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            k += 1
            if k > j:
                a[i], a[j], a[k] = a[k], a[i], a[j]
            else:
                a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    randomized_quick_sort2(a, l, m - 1)
    randomized_quick_sort2(a, m + 1, r)


def stress_test():
    from itertools import count

    for n in count(100, 100):
        a = [random.randint(0, 5) for _ in range(n)]
        sanity_check = sorted(a)
        randomized_quick_sort(a, 0, n - 1)
        if sanity_check == a:
            print(n, end='\r', flush=True)
        else:
            print('Failed!')
            print(a)
            break


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
