from test_framework import generic_test


def search_first_of_k(A, k):
    L, H = 0, len(A)-1
    ans = -1
    while L <= H:
        M = L + (H - L) // 2
        if A[M] == k:
            ans = M
            H = M - 1
        elif A[M] < k:
            L = M + 1
        else:
            H = M - 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
