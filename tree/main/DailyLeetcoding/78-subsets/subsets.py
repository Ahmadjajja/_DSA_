class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(index, subset, res):
            if index >= len(nums):
                res.append(subset.copy())
                return res

            left = dfs(index + 1, subset + [nums[index]], res)
            right = dfs(index + 1, subset, left)

            return right
        
        return dfs(0, [], [])



        