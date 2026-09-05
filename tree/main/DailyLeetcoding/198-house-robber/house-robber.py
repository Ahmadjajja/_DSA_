class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]

            skip = dfs(index + 1)
            take = nums[index] + dfs(index + 2)

            cache[index] = max(skip, take)
            return cache[index]

        return dfs(0)