# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return

        lca = root

        while root:
            if p.val < root.val and q.val < root.val:
                left = self.lowestCommonAncestor(root.left, p, q)
                return left
            elif p.val > root.val and q.val > root.val:
                right = self.lowestCommonAncestor(root.right, p, q)
                return right
            else:
                break
        return lca