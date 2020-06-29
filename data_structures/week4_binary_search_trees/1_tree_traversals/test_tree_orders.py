from contextlib import contextmanager
import sys

import pytest

from tree_orders import TreeOrders


@pytest.fixture(params=['01', '02', '21'])
def index(request):
    return request.param


@pytest.fixture
def tree(index):
    tree = TreeOrders()
    with replace_stdin(open(f'tests/{index}')):
        tree.read()
    return tree


@pytest.fixture(params=['in', 'pre', 'post'])
def method(request):
    return f'{request.param}Order'


@pytest.fixture
def expected(index, method):
    output_index = {'inOrder': 0, 'preOrder': 1, 'postOrder': 2}[method]
    with open(f'tests/{index}.a') as f:
        for i in range(output_index):
            f.readline()
        return list(map(int, f.readline().split()))


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


# @pytest.mark.parametrize('index', ['01', '02'])
def test_TreeOrders(tree, method, expected):
    # tree = TreeOrders()

    # input_file = f'tests/{index}'
    # with replace_stdin(open(input_file)):
    #     tree.read()

    # print(tree.key)
    # output_file = f'{input_file}.a'
    # with open(output_file) as f:
    #     expected = [list(map(int, line.split())) for line in f]

    order = getattr(tree, method)
    assert order() == expected

    # assert tree.inOrder() == expected[0]
    # assert tree.preOrder() == expected[1]
    # assert tree.postOrder() == expected[2]
