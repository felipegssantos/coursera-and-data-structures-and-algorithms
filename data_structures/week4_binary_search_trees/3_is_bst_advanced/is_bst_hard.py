#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def is_binary_search_tree(tree):
    # empty tree is considered valid
    if not tree:
        return True
    return _is_bst(tree)


def _is_bst(tree):
    def is_ok(node, lbound, rbound):
        if lbound is None:
            return key(node) < rbound
        elif rbound is None:
            return lbound <= key(node)
        else:
            return lbound <= key(node) < rbound

    def key(index):
        return tree[index][0]

    def left(index):
        return tree[index][1]

    def right(index):
        return tree[index][2]

    # Initialize a stack with root's children, if they exist
    stack = []
    if left(0) > 0:
        stack.append((left(0), None, key(0)))
    if right(0) > 0:
        stack.append((right(0), key(0), None))
    # Traverse tree propagating bounds from parents to children
    while stack:
        node, left_bound, right_bound = stack.pop()
        if not is_ok(node, left_bound, right_bound):
            return False
        # Left (right) child is bounded by its parent left_bound (key)
        # on the left and by its parent key (right_bound) on the right
        if left(node) > 0:
            stack.append((left(node), left_bound, key(node)))
        if right(node) > 0:
            stack.append((right(node), key(node), right_bound))
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
