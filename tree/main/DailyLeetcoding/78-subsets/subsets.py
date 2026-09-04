class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(index, subset):
            # base case
            if index == len(nums):
                res.append(subset)
                return
            
            # skip
            dfs(index + 1, subset)
            dfs(index + 1, subset + [nums[index]])

        dfs(0, [])

        return res

        
        