class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (robbed, not_robbed)

            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            robbed = node.val + left_not + right_not
            not_robbed = max(left_rob, left_not) + max(right_rob, right_not)

            return (robbed, not_robbed)

        return max(dfs(root))
