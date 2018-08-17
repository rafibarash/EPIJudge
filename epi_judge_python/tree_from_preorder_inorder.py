from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    class BinaryTreeNode:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def findNode(node, arr):
        for i, n in enumerate(arr):
            if n == node:
                return i
        return -1

    # base case
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    # get current node
    cur_data = preorder[0]
    i = findNode(cur_data, inorder)
    # split inorder arrays into left and right
    left_preorder = preorder[1:i+1]
    right_preorder = preorder[i+1:]
    left_inorder = inorder[:i]
    right_inorder = inorder[i+1:]
    # build node
    node = BinaryTreeNode(cur_data)
    node.left = binary_tree_from_preorder_inorder(left_preorder, left_inorder)
    node.right = binary_tree_from_preorder_inorder(
        right_preorder, right_inorder)
    return node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
