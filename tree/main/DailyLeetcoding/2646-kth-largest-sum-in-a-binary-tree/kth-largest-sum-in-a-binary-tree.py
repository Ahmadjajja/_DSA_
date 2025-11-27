# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        hm = {}


        def dfs(node, index):
            if not node:
                return

            hm[index] = hm.get(index, 0) + node.val

            dfs(node.left, index + 1)
            dfs(node.right, index + 1)

        dfs(root, 0)
        
        if len(hm) < k:
            return -1

        print(hm)

        max_heap = []
        heapq.heapify(max_heap)
        for key, val in hm.items():
            heapq.heappush(max_heap, -val)

        ans = 0

        for i in range(k):
            ans = -heapq.heappop(max_heap)

        return ans
        