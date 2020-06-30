#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def is_binary_search_tree(tree):
    # empty tree is considered valid
    if not tree:
        return True

    # in-order traversal should return a sorted array
    in_order = traverse_in_order(tree)
    x1 = next(in_order)
    for x2 in in_order:
        if x2 < x1:
            return False
        x1 = x2
    return True


def traverse_in_order(tree):
    def key(index):
        return tree[index][0]

    def left(index):
        return tree[index][1]

    def right(index):
        return tree[index][2]

    stack = []
    i = 0
    while stack or i >= 0:
        while i >= 0:
            stack.append(i)
            i = left(i)
        if stack:
            i = stack.pop()
            yield key(i)
            i = right(i)


def key(tree, index):
    return tree[index][0]


def left_child(tree, index):
    return tree[index][1]


def right_child(tree, index):
    return tree[index][2]


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
