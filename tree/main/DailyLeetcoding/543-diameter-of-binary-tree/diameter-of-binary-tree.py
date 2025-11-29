# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]


            left = dfs(node.left)
            right = dfs(node.right)

            dia = max(left[1] + right[1], max(left[0], right[0]))
            maxDep = max(left[1], right[1])

            return [dia, maxDep + 1]

        return dfs(root)[0]
        