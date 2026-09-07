class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans
        