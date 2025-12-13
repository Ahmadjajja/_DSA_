# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, ans):
            if not ans:
                return [0, ans]
            if not node:
                return [0, ans]

            
            left = dfs(node.left, ans)
            right = dfs(node.right, ans)

            if not left[1] or not right[1]:
                return [0, False]

            if abs(left[0] - right[0]) > 1:
                return [0, False]
            
            return [max(left[0], right[0]) + 1, True]

        return dfs(root, True)[1]

# tc: O(n)
# sc: O(h)
        