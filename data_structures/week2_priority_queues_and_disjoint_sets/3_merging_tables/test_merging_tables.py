import pytest

from merging_tables import Database


@pytest.mark.parametrize('index', [('01'), ('02'), ('116')])
def test_assign_jobs(index):
    with open(f'tests/{index}') as f:
        n_tables, n_queries = list(map(int, f.readline().split()))
        counts = list(map(int, f.readline().split()))
        assert len(counts) == n_tables
        merges = [tuple(map(int, line.split())) for line in f]
        assert len(merges) == n_queries

    db = Database(counts)
    result = []
    for dst, src in merges:
        db.merge(dst - 1, src - 1)
        result.append(db.max_row_count)

    with open(f'tests/{index}.a') as f:
        expected = [int(i) for i in f]

    assert result == expected
