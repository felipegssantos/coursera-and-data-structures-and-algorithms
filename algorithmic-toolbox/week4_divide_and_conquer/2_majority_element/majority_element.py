# Uses python3
import sys


def get_majority_element(a, left, right) -> int:
    if left == right:  # reached end of array
        return -1
    if left + 1 == right:  # found array of length 1
        return a[left]

    middle = (left + right) // 2
    left_maj = get_majority_element(a, left, middle)
    right_maj = get_majority_element(a, middle, right)

    # If both halves agree about majority element, the answer is trivial
    if left_maj == right_maj:
        return left_maj
    # If halves do not agree about majority element, check in the array
    # whether any of the candidate answers is correct
    else:
        if left_maj + 1 > 0:
            counts = sum(1 for x in a[left:right] if x == left_maj)
            if counts > (right - left) / 2:
                return left_maj
        if right_maj + 1 > 0:
            counts = sum(1 for x in a[left:right] if x == right_maj)
            if counts > (right - left) / 2:
                return right_maj
    return -1


def check(a, n) -> int:
    from collections import Counter
    counter = Counter(a)
    most_common, counts = counter.most_common(1)[0]
    if counts > n/2:
        return most_common
    else:
        return -1


def stress_test():
    # from random import randint
    # for n in range(int(1e5) - 1, int(1e5)):
    n = int(1e5)
    a1 = ([int(1e9)] * (n//2)) + ([int(1e9) - 1] * (n//2))
    a2 = [int(1e9) + i for i in range(n)]
    for a in [a1, a2]:
        # a = [randint(0, 10) for _ in range(n)]
        out = get_majority_element(a, 0, n)
        maj = check(a, n)
        if out == maj:
            print(n, end='\r', flush=True)
        else:
            print('Failed')
            print(n, a)
            print(maj, out)
            raise RuntimeError('Failed')


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
