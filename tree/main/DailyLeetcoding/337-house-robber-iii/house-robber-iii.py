class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """Returns (max_if_robbed, max_if_not_robbed) for the subtree rooted at node."""
            if not node:
                return 0, 0

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob = node.val + left_skip + right_skip
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob, skip

        return max(dfs(root))