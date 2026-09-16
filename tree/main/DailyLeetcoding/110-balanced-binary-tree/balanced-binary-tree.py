# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
            
            left = dfs(node.left)
            right = dfs(node.right)

            if not (left[1] and right[1]) or abs(left[0] - right[0]) > 1:
                return [0, False]

            return [1 + max(left[0], right[0]), True]

        return dfs(root)[1]
        