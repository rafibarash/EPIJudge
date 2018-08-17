from test_framework import generic_test


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def merge_two_sorted_lists(L1, L2):
    head = runner = ListNode(0)
    while L1 and L2:
        if L1.data < L2.data:
            runner.next = L1
            L1 = L1.next
        else:
            runner.next = L2
            L2 = L2.next
        runner = runner.next
    runner.next = L1 or L2
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
