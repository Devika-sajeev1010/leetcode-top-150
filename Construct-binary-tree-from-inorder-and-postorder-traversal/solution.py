# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            # Build right subtree first
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)