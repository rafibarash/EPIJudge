from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    head = slow_runner = fast_runner = L
    while k != 0:
        fast_runner = fast_runner.next
        k -= 1
    if (not fast_runner):
        return head.next
    while (fast_runner.next):
        slow_runner, fast_runner = slow_runner.next, fast_runner.next
    slow_runner.next = slow_runner.next.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
