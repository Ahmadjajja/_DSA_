class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                return [hm[nums[i]], i]

            otherElemToFind = target - nums[i]
            hm[otherElemToFind] = i
        
        return [-1, -1]