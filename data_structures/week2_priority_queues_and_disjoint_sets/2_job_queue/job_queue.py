# python3

from collections import namedtuple
from heapq import heapify, heappush, heappop


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


def assign_jobs(n_workers, jobs):
    queue = [Worker(i, 0) for i in range(n_workers)]
    heapify(queue)

    result = []
    for job in jobs:
        worker = heappop(queue)
        result.append(AssignedJob(worker.id, worker.next_free_time))
        heappush(queue, Worker(worker.id, worker.next_free_time+job))

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
