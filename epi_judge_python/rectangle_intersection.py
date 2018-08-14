import collections
import math

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    # TODO - you fill in here.
    # one rectangle should have x point that is greater than other x but less than other x + other width
    # y point should be like that too
    R1x = R1[0]
    R1y = R1[1]
    R1w = R1[2]
    R1h = R1[3]
    R2x = R2[0]
    R2y = R2[1]
    R2w = R2[2]
    R2h = R2[3]
    dumb = 0
    # r1x is small
    if (R1x > R2x & R1x < R2x + R2w):
        smallx = R1
        bigx = R2
    # r2x is small
    elif (R2x > R1x & R2x < R1x + R1w):
        smallx = R2
        bigx = R1
    else:
        dumb += 1
    # r1y is small
    if (R1y > R2y & R1y < R2y + R2h):
        smally = R1
        bigy = R2
    # r2y is small
    elif (R2y > R1y & R2y < R1y + R1h):
        smally = R2
        bigy = R1
    # no overlap
    else:
        dumb += 1
    if dumb == 2:
        return Rectangle(0, 0, -1, -1)
    x_bound = min(smallx[0]+smallx[2], bigx[0]+bigx[2])
    x = x_bound - smallx[0]
    y_bound = min(smally[1]+smally[3], bigy[1]+bigx[2])
    y = y_bound - smally[1]
    return Rectangle(smallx[0], smally[1], x, y)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
