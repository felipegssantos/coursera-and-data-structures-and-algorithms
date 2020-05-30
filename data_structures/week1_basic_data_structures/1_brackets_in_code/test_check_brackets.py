import pytest

from check_brackets import find_mismatch


@pytest.mark.parametrize('text, expected',
                         [('[]', 'Success'),
                          ('{}[]', 'Success'),
                          ('[()]', 'Success'),
                          ('(())', 'Success'),
                          ('{[]}()', 'Success'),
                          ('{', 1),
                          ('{[}', 3),
                          ('foo(bar);', 'Success'),
                          ('foo(bar[i);', 10),
                          ('}', 1)])
def test_find_mismatch(text, expected):
    assert find_mismatch(text) == expected
