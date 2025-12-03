# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            s = node.val + left + right
            maxPath = max(maxPath, s)

            value_to_send_back = node.val + max(left, right)

            if value_to_send_back > 0:
                return value_to_send_back
            
            return 0
        
        dfs(root)
        return maxPath
        