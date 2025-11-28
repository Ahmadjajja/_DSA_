# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         # 0: [3],
#         # 1: [9, 20],
#         # 2: [15, 7]
#         hm = {}

#         def dfs(node, lvl):
#             # base case
#             if not node:
#                 return
            
#             if lvl in hm:
#                 hm[lvl].append(node.val)
#             else:
#                 hm[lvl] = [node.val]
            
#             dfs(node.left, lvl + 1)
#             dfs(node.right, lvl + 1) 

        
#         dfs(root, 0)

#         for key, val in hm.items():
#             res.append(val)
        
#         return res
        
# # tc : O(n + lvls) = O(n)
# # sc : O(n + n) = O(n)


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res
