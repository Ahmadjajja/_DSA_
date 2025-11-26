class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # value -> index

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i

        return [-1, -1]
