class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = {}

        # def dfs(index):
        #     if index >= len(nums):
        #         return 0
        #     if index in cache:
        #         return cache[index]

        #     skip = dfs(index + 1)
        #     take = nums[index] + dfs(index + 2)

        #     cache[index] = max(skip, take)
        #     return cache[index]

        # return dfs(0)

        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
