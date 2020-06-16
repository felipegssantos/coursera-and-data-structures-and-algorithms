# python3

from collections import namedtuple


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:

    def __init__(self, id, next_free_time):
        self.id = id  # must be careful to pass an unused id value
        self.next_free_time = next_free_time

    def __lt__(self, other):
        if self.next_free_time == other.next_free_time:
            return self.id < other.id
        else:
            return self.next_free_time < other.next_free_time

    def __gt__(self, other):
        return not self.__gt__(other)


class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, x):
        self.heap.append(x)
        if self.size > 0:
            # Sift up until heap property is recovered
            current = self.size
            parent = (current-1) // 2
            while current > 0 and self.heap[current] > self.heap[parent]:
                self.heap[current], self.heap[parent] =\
                    self.heap[parent], self.heap[current]
                current = parent
                parent = (current-1) // 2
        self.size += 1

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        *self.heap, maximum = self.heap
        self.size -= 1
        if self.size > 0:
            # Sift down until heap property is recovered
            current = 0
            children = [c for c in [1, 2] if c < self.size]
            while any([self.heap[current] < self.heap[child]
                       for child in children]):
                if len(children) == 1:
                    largest = children[0]
                else:
                    left, right = children
                    if self.heap[left] > self.heap[right]:
                        largest = left
                    else:
                        largest = right
                self.heap[current], self.heap[largest] =\
                    self.heap[largest], self.heap[current]
                current = largest
                children = [c for c in [2*current+1, 2*current+2]
                            if c < self.size]
        return maximum


def assign_jobs(n_workers, jobs):
    queue = PriorityQueue()
    for i in range(n_workers):
        queue.insert(Worker(i, 0))

    result = []
    for job in jobs:
        worker = queue.extract_max()
        result.append(AssignedJob(worker.id, worker.next_free_time))
        queue.insert(Worker(worker.id, worker.next_free_time+job))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
