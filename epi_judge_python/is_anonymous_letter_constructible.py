from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # l = Counter(letter_text)
    # m = Counter(magazine_text)
    # for k, v in l.items():
    #     if m[k] < v:
    #         return False
    # return True
    return (not Counter(letter_text) - Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
