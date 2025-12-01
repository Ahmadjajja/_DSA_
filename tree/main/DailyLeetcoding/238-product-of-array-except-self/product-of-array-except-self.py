class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [nums[i] for i in range(len(nums))]

        # [1, 2, 3, 4] -> origional
        # [1, 1, 2, 6] -> prefix
        # [24 , 12, 4, 1] -> suffix

        # prefix
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        print("prefix -> ", output)
        # suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix *= nums[i]
        print("prefix -> ", output)

        

        return output

        