# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            output.append(root.val)
            in_order(root.right)
        in_order(root)
        return output[k-1]

        