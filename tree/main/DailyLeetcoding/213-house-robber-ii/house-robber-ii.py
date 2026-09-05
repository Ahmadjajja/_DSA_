class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1 or length == 2 or length == 3:
                return max(nums)
        
        def helper(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(helper(nums[1:]), helper(nums[:-1]))