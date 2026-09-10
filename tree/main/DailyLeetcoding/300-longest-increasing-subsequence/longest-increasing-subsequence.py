# top down

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        return max(dfs(i) for i in range(n))

# # bottom up

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         LIS = [1] * len(nums)

#         for i in range(len(nums) - 1, -1, -1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] < nums[j]:
#                     LIS[i] = max(LIS[i], 1 + LIS[j])
#         return max(LIS)

        