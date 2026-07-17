# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # METHOD 1: Recursion
        if not root:
            return None
        # if both p and q val are less than current root.val then " move to left child "
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if both p and q val are greater than current roo.val then " move to right child "
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # else return the current root node as it is the LCA
        return root

        # METHOD 2: Iterative
        # cur = root

        # while cur:
        #     if p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     elif p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     else:
        #         return cur