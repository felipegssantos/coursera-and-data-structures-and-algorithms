# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, start=1):
        if next in "([{":
            opening_brackets_stack.append((i, next))
        elif next in ")]}":
            try:
                _, last_opened = opening_brackets_stack.pop()
                if not are_matching(last_opened, next):
                    return i
            except IndexError:
                return i

    if len(opening_brackets_stack) > 0:
        i, _ = opening_brackets_stack.pop(0)
        return i
    else:
        return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
