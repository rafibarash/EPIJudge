from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s):
    # d = {}
    # one_odd = False
    # for ch in s:
    #     if ch in d:
    #         d[ch] += 1
    #     else:
    #         d[ch] = 1
    # for val in d.values():
    #     if val & 1:
    #         if one_odd:
    #             return False
    #         one_odd = True
    # return True
    return sum(v % 2 for v in Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
