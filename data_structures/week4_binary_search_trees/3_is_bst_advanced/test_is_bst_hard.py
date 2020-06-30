from contextlib import contextmanager
import sys

import pytest

from is_bst_hard import is_binary_search_tree


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


@pytest.fixture(params=['01', '02', '03', '04', '05', '06', '07', '08', '09'])
def index(request):
    return request.param


@pytest.fixture
def tree(index):
    with replace_stdin(open(f'tests/{index}')):
        nodes = int(sys.stdin.readline().strip())
        tree = []
        for i in range(nodes):
            tree.append(list(map(int, sys.stdin.readline().strip().split())))
    return tree


@pytest.fixture
def expected(index):
    with open(f'tests/{index}.a') as f:
        answer = f.read().strip()
    if answer == 'CORRECT':
        return True
    elif answer == 'INCORRECT':
        return False
    else:
        raise ValueError(f'Wrong answer file for index={index}')


def test_is_binary_search_tree(tree, expected):
    assert is_binary_search_tree(tree) == expected
