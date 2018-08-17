import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    x = A[pivot_index]
    beg, end = 0, len(A) - 1
    # First pass:
    # set all values less than or equal to x on left
    # set all greater values on right of array
    while beg < end:
        if A[beg] <= x:
            beg += 1
        else:
            A[beg], A[end] = A[end], A[beg]
            end -= 1
    beg, end = 0, len(A) - 1
    # Second pass:
    # set end = index of first elemet less than or equal to x
    # if A[beg] == x, swap and decrement end
    # otherwise increment beg
    while beg < end:
        if A[end] > x:
            end -= 1
        else:
            if A[beg] == x:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
            else:
                beg += 1
    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
