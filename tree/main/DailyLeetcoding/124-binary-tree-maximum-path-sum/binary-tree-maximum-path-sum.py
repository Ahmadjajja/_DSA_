# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, float('-inf')]
            
            left = dfs(node.left)
            right = dfs(node.right)

            s = node.val + left[0] + right[0]
            maxPath = max(max(left[1], right[1]), s)

            value_to_send_back = node.val + max(left[0], right[0])

            if value_to_send_back > 0:
                return [value_to_send_back, maxPath]
            
            return [0, maxPath]
        
        return dfs(root)[1]
        