class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index, sum):
            if index >= len(nums):
                return sum
            
            if (index, sum) in cache:
                return cache[(index, sum)]
            
            # skip
            left = dfs(index + 1, sum)
            # choose
            right = dfs(index + 2, sum + nums[index])

            cache[(index, sum)] = max(left, right)

            return cache[(index, sum)]
        
        return dfs(0, 0)
        