# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if root is None:
                return
            traverse(root.left)

            self.prev.right = root
            root.left = None
            self.prev = root

            traverse(root.right)

        dummY = TreeNode()
        self.prev = dummY

        traverse(root)
        
        return dummY.right

        