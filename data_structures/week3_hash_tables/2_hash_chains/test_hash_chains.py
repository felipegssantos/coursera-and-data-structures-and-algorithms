import pytest

from hash_chains import Query, QueryProcessor


def fetch_data():
    for i in ['01', '02', '06']:
        # Fetch input
        with open(f'tests/{i}') as f:
            num_buckets = int(f.readline())
            num_queries = int(f.readline())
            queries = [Query(line.split()) for line in f]
        assert len(queries) == num_queries
        # Fetch output
        with open(f'tests/{i}.a') as f:
            result = [line.strip() for line in f]
        yield num_buckets, queries, result


@pytest.mark.parametrize('m, queries, expected', list(fetch_data()))
def test_process_queries(m, queries, expected):
    assert QueryProcessor(m).process_queries(queries) == expected
