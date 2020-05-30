#Uses python3

import sys


def largest_number(a):
    res = ""
    while a:
        max_digit = a[0]
        for x in a[1:]:
            if is_greater_or_equal(x, max_digit):
                max_digit = x
        res += max_digit
        a.remove(max_digit)
    return res


def is_greater_or_equal(x, y) -> bool:
    return int(x+y) >= int(y+x)


def is_greater_or_equal_alt(x, y) -> bool:
    if y is None:
        return True

    if len(x) > len(y):
        x = x[:len(y)+1]
        y += y[0]
    elif len(x) < len(y):
        y = y[:len(x)+1]
        x += x[0]

    return int(x) >= int(y)


def stress_test():
    from random import randint
    while True:
        a = [str(randint(1, 9999)), str(randint(1, 9999))]
        y = is_greater_or_equal(*a)
        y_alt = is_greater_or_equal_alt(*a)
        if y == y_alt:
            print('ok')
        else:
            print('Error!')
            print(f'a={a}, y={y}, y_alt={y_alt}')
            break


if __name__ == '__main__':
    # stress_test()
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
