from test_framework import generic_test


def parity(x):
    ans = 0
    while x:
        ans += x & 1
        x >>= 1
    return 1 if ans & 1 else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
