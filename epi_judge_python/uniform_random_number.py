import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound, upper_bound):
    n_flips = math.ceil(math.log2(upper_bound - lower_bound))
    if n_flips == 0:
        n_flips = 1
    done = False
    while not done:
        b_mask = ''
        for i in range(n_flips):
            b_mask += str(zero_one_random())
        p = 1
        ans = lower_bound
        for ch in b_mask:
            ans += int(ch)*p
            p *= 2
        if ans <= upper_bound:
            done = True
    return ans



@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(lambda : [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound
             for a in result], upper_bound - lower_bound + 1, 0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("uniform_random_number.py",
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
