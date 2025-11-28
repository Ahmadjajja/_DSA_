# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

    #     9
    #     /\
    #    7  10


    #    2nd lvl values 
    #    7, 10, 15, 7
    #    7, 15, 10, 7 or (10, 7), (7, 15)
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
            if i % 2 == 1:
                res.append(hm[i][::-1])
            else:
                res.append(hm[i])
        
        return res
        