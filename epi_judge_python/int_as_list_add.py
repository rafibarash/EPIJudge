from test_framework import generic_test

class ListNode():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def add_two_numbers(L1, L2):
    head = sum = ListNode()
    p = 0
    while L1 or L2:
        x = 0
        y = 0
        if (L1):
            x = L1.data
            L1 = L1.next
        if (L2):
            y = L2.data
            L2 = L2.next
        n = x + y + p
        p = 1 if n >= 10 else 0
        sum.data = n % 10
        sum.next = None if not L1 and not L2 else ListNode()
        sum = sum.next
    # append end of list
    run = head
    while run:
        print(run.data)
        run = run.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
