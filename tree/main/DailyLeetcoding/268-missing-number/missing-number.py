class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n  # start with n, since range is [0, n] but index only covers [0, n-1]

        for i in range(n):
            result ^= i ^ nums[i]

        return result