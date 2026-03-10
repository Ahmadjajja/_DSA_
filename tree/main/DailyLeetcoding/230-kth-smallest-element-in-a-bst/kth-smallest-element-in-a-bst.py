# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        counter = 0
        def dfs(node):
            nonlocal ans, counter

            if not node:
                return

            dfs(node.left)
            if counter + 1 == k:
                ans = node.val
            counter += 1
            dfs(node.right)

            return

        dfs(root)

        return ans
        