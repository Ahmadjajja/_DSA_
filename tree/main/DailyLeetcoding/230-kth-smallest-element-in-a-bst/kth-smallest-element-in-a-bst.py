# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal k
            if not node:
                return 'A'

            left = dfs(node.left)
            if left != 'A':
                return left
            k -= 1
            if k == 0:
                return node.val
            right = dfs(node.right)
            if right != 'A':
                return right

            return 'A'

        
        return dfs(root)