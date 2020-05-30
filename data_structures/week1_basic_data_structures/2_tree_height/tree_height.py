# python3
import sys
import threading


def compute_height(n, parents):
    # Build the tree
    tree = {node: [] for node in range(n)}
    for node in range(n):
        parent = parents[node]
        if parent == -1:
            root = node
        else:
            tree[parent].append(node)

    # Compute height
    node_stack = [(1, root)]
    max_height = 0
    while node_stack:
        height, node = node_stack.pop()
        children = tree[node]
        if children:
            for child in children:
                node_stack.append((height+1, child))
        else:
            max_height = max(max_height, height)

    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
