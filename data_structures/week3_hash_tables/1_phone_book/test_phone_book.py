import pytest

from phone_book import process_queries, Query


def fetch_data():
    for i in ['01', '02']:
        # Fetch input
        with open(f'tests/{i}') as f:
            num_queries = int(f.readline())
            queries = [Query(line.split()) for line in f]
        assert len(queries) == num_queries
        # Fetch output
        with open(f'tests/{i}.a') as f:
            result = [line.strip() for line in f]
        yield queries, result


@pytest.mark.parametrize('queries, expected', list(fetch_data()))
def test_process_queries(queries, expected):
    assert process_queries(queries) == expected
