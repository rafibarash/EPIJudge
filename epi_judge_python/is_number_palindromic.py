from test_framework import generic_test


def is_palindrome_number(x):
    return str(x) == str(x)[::-1]
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
