class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root, maxi, mini):
            if root is None:
                return maxi - mini
            maxi = max(maxi, root.val)
            mini = min(mini, root.val)
            left = traverse(root.left, maxi, mini)
            right = traverse(root.right, maxi, mini)
            return max(left, right)
        
        return traverse(root, root.val, root.val)
