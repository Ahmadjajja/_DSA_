# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hm = {}

        def dfs(node,lvl):
            if not node:
                return
            
            if lvl in hm:
                hm[lvl].append(node.val)
            else:
                hm[lvl] = [node.val]
            
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        
        dfs(root, 0)
        res = []
        for key, val in hm.items():
            res.append(val[len(val) - 1])

        return res