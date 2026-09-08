class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, res):
            if i == len(nums):
                if res == target:
                    return 1
                else:
                    return 0
            
            if (i, res) in cache:
                return cache[(i, res)]
            
            left = dfs(i + 1, res - nums[i])
            right = dfs(i + 1, res + nums[i])

            cache[(i, res)] = left + right
            
            return cache[(i, res)]

        return dfs(0, 0)
        