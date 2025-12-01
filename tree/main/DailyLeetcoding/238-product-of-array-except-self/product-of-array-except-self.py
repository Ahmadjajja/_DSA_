class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [nums[i] for i in range(len(nums))]

        # prefix
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        # suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix *= nums[i]

        return output

        