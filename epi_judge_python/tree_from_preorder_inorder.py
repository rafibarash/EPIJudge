from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    
    # root is preorder[0]
    # all elements left of root in inorder are left, all right are right
    # if preorder[1] is left of 
    def build_tree(parent, preorder, inorder):
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        if not parent:
            parent = Node(data = preorder[0])
        i = inorder.index(preorder[0])
        l_index = 
        left = build_tree(parent, preorder[1:], inorder[0:i])
        right = build_tree(parent, preorder[1:], inorder[i+1:])
        parent.left = left
        parent.right = right
        i = inorder.index(preorder[0])
        node = Node(preorder[0])

        
    return build_tree(None, preorder, inorder)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
