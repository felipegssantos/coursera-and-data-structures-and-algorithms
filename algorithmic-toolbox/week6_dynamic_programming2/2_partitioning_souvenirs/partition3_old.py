# Uses python3
import sys


def partition3(A):
    # If A has less than 3 elements or sum(A) is not divisible by zero,
    # there is no solution
    total_value = sum(A)
    if len(A) < 3 or total_value % 3 > 0:
        return 0

    W = total_value // 3
    for _ in range(3):
        values = sub_knapsack(W, A)
        if values:
            for v in values:
                A.remove(v)
        else:
            return 0

    return 1


def sub_knapsack(W, w):
    """Tries to find a solution to the knapsack problem with
    v[i] = w[i] for all i and such that the full knapsack capacity
    is filled.

    Arguments:
        W {int} -- the knapsack capacity
        w {list of ints} -- list of item weights

    Returns:
        list of ints -- weights of the items used in the knapsack
            (returns an empty list if there is no solution using
             the full knapsack capacity)
    """
    values = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]
    for i in range(len(w)):
        for j in range(1, W+1):
            if j >= w[i] and values[i][j-w[i]] + w[i] > values[i][j]:
                values[i+1][j] = values[i][j-w[i]] + w[i]
            else:
                values[i+1][j] = values[i][j]

    if values[-1][-1] == W:
        # Reconstructing: get items placed in the knapsack
        solution = []
        j = W
        i = len(w) - 1
        while j > 0:
            if values[i+1][j] == values[i][j]:
                pass
            elif j >= w[i]:
                solution.append(w[i])
                j = j - w[i]
            else:
                break
            i -= 1
        return solution
    else:
        return []


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
