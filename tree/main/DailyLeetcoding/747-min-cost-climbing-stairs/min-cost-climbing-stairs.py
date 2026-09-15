class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # top-down approach
        memo = {}
        def dfs(index):
            if index >= len(cost):
                return 0
            
            if index in memo:
                return memo[index]

            left = dfs(index + 1)
            right = dfs(index + 2)

            memo[index] = cost[index] + min(left, right)

            return memo[index]
        
        return min(dfs(0), dfs(1))