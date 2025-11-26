class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            nextElem = target - nums[i]
            hashmap[nextElem] = i

        return [-1, -1]

# tc: O(n)  
# sc: O(n)