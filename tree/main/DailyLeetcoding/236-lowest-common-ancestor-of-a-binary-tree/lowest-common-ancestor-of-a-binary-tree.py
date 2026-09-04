class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None

            # If we hit p or q, just return it upward
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # If both sides non-empty, this node is the LCA
            if left and right:
                return node

            # Otherwise propagate the non-null one (either p/q or an LCA below)
            return left if left else right

        return dfs(root)