class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            rob_this = nums[i] + dfs(i + 2)
            skip_this = dfs(i + 1)
            
            memo[i] = max(rob_this, skip_this)
            return memo[i]
        
        return dfs(0)
