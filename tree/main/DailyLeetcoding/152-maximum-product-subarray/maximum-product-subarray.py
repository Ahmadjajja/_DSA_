class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix, suffix = 0, 0
        n, res = len(nums), nums[0]

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(res, prefix, suffix)
        
        return res