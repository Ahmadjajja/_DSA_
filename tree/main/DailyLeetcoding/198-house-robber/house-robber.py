class Solution:
    def rob(self, nums: List[int]) -> int:
        # # top-down
        # memo = {}
        
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     rob_this = nums[i] + dfs(i + 2)
        #     skip_this = dfs(i + 1)
            
        #     memo[i] = max(rob_this, skip_this)
        #     return memo[i]
        
        # return dfs(0)
        # bottom-up approach

        if len(nums) == 1:
            return nums[0]

        first, second = 0, 0
        for num in nums:
            cur = max(first + num, second)
            first = second
            second = cur
        return second

