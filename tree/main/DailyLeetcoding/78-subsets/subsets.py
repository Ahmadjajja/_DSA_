class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, subset):
            nonlocal res
            if index >= len(nums):
                res.append(subset.copy())
                return
            dfs(index + 1, subset + [nums[index]])
            dfs(index + 1, subset)
        
        dfs(0, [])

        return res



        