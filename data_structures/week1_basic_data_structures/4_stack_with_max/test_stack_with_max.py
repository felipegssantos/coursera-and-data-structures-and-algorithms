from pathlib import Path

import pytest

from stack_with_max import StackWithMax


@pytest.fixture(params=list(range(1, 6)))
def input_output(request):
    path = Path(__file__, '../tests').resolve()
    i_str = str(request.param).rjust(2, '0')
    input_path = Path(path, i_str)
    answer_path = Path(path, f'{i_str}.a')
    return load_input(input_path), load_answer(answer_path)


def load_input(path):
    with open(path) as f:
        return [line.split() for line in f]


def load_answer(path):
    with open(path) as f:
        return [int(n) for n in f]


def test_stack_with_max(input_output):
    queries, answers = input_output
    n = queries.pop(0)[0]
    stack = StackWithMax()

    for i in range(int(n)):
        query = queries[i]

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
