from test_framework import generic_test
from math import floor, sqrt


def square_root(k):
    # lol fast way to do it without searching
    return floor(sqrt(k))
    # but with searching ......


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
