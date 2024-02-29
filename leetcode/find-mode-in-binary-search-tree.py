from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(node):
            nonlocal max_freq, count, modes
            if node is None:
                return
            inorder_traversal(node.left)
            count[node.val] += 1
            max_freq = max(max_freq, count[node.val])
            inorder_traversal(node.right)
        
        if root is None:
            return []
        
        count = defaultdict(int)
        max_freq = 0
        inorder_traversal(root)
        
        modes = [key for key, value in count.items() if value == max_freq]
        return modes
