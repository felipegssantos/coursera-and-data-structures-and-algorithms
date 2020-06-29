# python3

import sys


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        stack = []  # this stack will track the traversed nodes
        i = 0
        while stack or i >= 0:
            # Go down the tree from node i until its leftmost leaf
            while i >= 0:
                stack.append(i)
                i = self.left[i]
            # Remove leftmost leaf and move to its right sibling if it exists
            if stack:
                i = stack.pop()
                result.append(self.key[i])
                i = self.right[i]
        return result

    def preOrder(self):
        result = []
        stack = [0]  # this stack will track the traversed nodes
        while stack:
            # Go down the tree always adding current node to result
            i = stack.pop()
            result.append(self.key[i])
            # Appending order ensures that left child will show up first
            for child in [self.right[i], self.left[i]]:
                if child > 0:
                    stack.append(child)
        return result

    def postOrder(self):
        reverse_result = []
        stack = [0]  # this stack will track the traversed nodes
        while stack:
            # Go down the tree always adding current node to reversed result
            # (i.e., to the end of the actual result)
            i = stack.pop()
            reverse_result.append(self.key[i])
            # Appending order ensures that right child will show up first
            # in reversed result
            for child in [self.left[i], self.right[i]]:
                if child > 0:
                    stack.append(child)
        return list(reversed(reverse_result))


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))
