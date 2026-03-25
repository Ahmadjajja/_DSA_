class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for index in range(len(nums)):
            if nums[index] in hm:
                return [index, hm[nums[index]]]

            hm[target - nums[index]] = index
        
        return [-1, -1]

        