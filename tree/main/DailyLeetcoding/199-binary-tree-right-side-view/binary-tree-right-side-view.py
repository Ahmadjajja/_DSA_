# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # 0: [1],
        # 1: [2, 3]
        # 2: [4]
        # 3: [5]

        # [1, 3, 4, 5]
        
        res = []
        hm = {}

        def dfs(node, lvl):
            # base case
            if not node:
                return
            
            if lvl in hm:
                hm[lvl].append(node.val)
            else:
                hm[lvl] = [node.val]
            
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)


        dfs(root, 0)

        for i in range(len(hm)):
            res.append(hm[i][-1])
        
        return res


