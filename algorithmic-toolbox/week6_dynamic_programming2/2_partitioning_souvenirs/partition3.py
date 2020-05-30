# Uses python3
from collections import defaultdict
from itertools import product
import sys


def partition3_iter(A):
    """Solution for souvenir partitions problem using an iterative
    dynamic programming algorithm.

    Arguments:
        A {list of ints} -- list of values to partition equally in
            3 subsets

    Returns:
        int -- 1 if it is possible to partition in 3 subsets of same
            summed value; 0 otherwise
    """
    # If A has less than 3 elements or sum(A) is not divisible by 3,
    # there is no solution
    total_value = sum(A)
    if len(A) < 3 or total_value % 3 > 0:
        return 0

    result = defaultdict(lambda: False)
    result[(0, 0, 0, 0)] = True

    W = total_value // 3
    sum_lists = 3 * [range(W+1)]
    for n in range(len(A)):
        for x, y, z in product(*sum_lists):
            result[(x, y, z, n+1)] = any([result[(x - A[n], y, z, n)],
                                          result[(x, y - A[n], z, n)],
                                          result[(x, y, z - A[n], n)]])
            print(f'result[({x}, {y}, {z}, {n+1})]={result[(x, y, z, n+1)]}')

    return int(result[(W, W, W, len(A))])


def partition3_recursive(A, a, b, c, n, cache):
    # Lookup the cache to avoid doing the same operation more than once
    if (a, b, c, n) in cache:
        return cache[(a, b, c, n)]
    # Stop condition: if all elements were used, partitioning is possible
    # only if all subsets reached zero summed value
    elif n == 0:
        return a == b == c == 0
    # Return false if any of the subsets exceeded the expected amount
    elif a < 0 or b < 0 or c < 0:
        return False
    else:
        # Try to find a solution placing the n-th element in the first subset;
        # if it does, return early
        first_try = partition3_recursive(A, a-A[n-1], b, c, n-1, cache)
        if first_try:
            return True

        # Try to find a solution placing the n-th element in the second subset;
        # return early if it does
        second_try = partition3_recursive(A, a, b-A[n-1], c, n-1, cache)
        if second_try:
            return True

        # Try to find a solution placing the n-th element in the third subset
        third_try = partition3_recursive(A, a, b, c-A[n-1], n-1, cache)
        return third_try


def partition3(A):
    # If A has less than 3 elements or sum(A) is not divisible by 3,
    # there is no solution
    total_value = sum(A)
    if len(A) < 3 or total_value % 3 > 0:
        return 0

    W = total_value // 3
    cache = {}
    result = partition3_recursive(A, W, W, W, len(A), cache)
    return int(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
