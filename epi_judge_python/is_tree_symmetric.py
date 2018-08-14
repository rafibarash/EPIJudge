from test_framework import generic_test


def is_symmetric(tree):
    def symmetric_children(l, r):
        if l and r:
            return (l.data == r.data
                   and symmetric_children(l.right, r.left)
                   and symmetric_children(l.left, r.right))
        if not l and not r:
            return True
        return False
    return symmetric_children(tree.left, tree.right) if tree else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
