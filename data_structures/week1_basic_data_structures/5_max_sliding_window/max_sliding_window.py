# python3
class StackWithMax():

    def __init__(self):
        self.__stack = []
        self.__max = []

    def append(self, a):
        if self.__max:
            current_max = self.__max[-1]
            if a > current_max:
                self.__max.append(a)
            else:
                self.__max.append(current_max)
        else:
            self.__max.append(a)
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__max.pop()
        return self.__stack.pop()

    def max(self):
        if self.__stack:
            return self.__max[-1]

    def __bool__(self):
        return bool(self.__stack)

    def __repr__(self):
        return f'StackWithMax({self.__stack})'


class StackedQueue:

    def __init__(self):
        self.stack1 = StackWithMax()
        self.stack2 = StackWithMax()

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                poped = self.stack1.pop()
                self.stack2.append(poped)
        return self.stack2.pop()

    def max(self):
        return max([x for x in [self.stack1.max(), self.stack2.max()]
                    if x is not None])


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window(sequence, m):
    queue = StackedQueue()

    for x in sequence[:m]:
        queue.enqueue(x)

    maximums = [queue.max()]
    for x in sequence[m:]:
        queue.dequeue()
        queue.enqueue(x)
        maximums.append(queue.max())

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
