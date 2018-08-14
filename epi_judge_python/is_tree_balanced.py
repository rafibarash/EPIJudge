from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def height(tree):
        return 0 if not tree else max(1 + height(tree.left), 1 + height(tree.right))

    if not tree:
        return True
    l = height(tree.left)
    r = height(tree.right)
    return abs(l - r) <= 1 and \
           is_balanced_binary_tree(tree.left) and \
           is_balanced_binary_tree(tree.right)
           


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
