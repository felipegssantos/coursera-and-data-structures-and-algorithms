import pytest

from job_queue import assign_jobs, AssignedJob


@pytest.mark.parametrize('index', [('02'), ('08')])
def test_assign_jobs(index):
    with open(f'tests/{index}') as f:
        n_workers, n_jobs = list(map(int, f.readline().split()))
        jobs = list(map(int, f.readline().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    with open(f'tests/{index}.a') as f:
        expected = [AssignedJob(*list(map(int, line.split()))) for line in f]

    assert assigned_jobs == expected
