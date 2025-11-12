class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        def dfs(i, p):
            if i > len(nums):
                return 
            if i == len(nums):
                res.append(p)
                return
            
            dfs(i + 1, p + [nums[i]])

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, p)

        dfs(0, [])
        print(res)

        return res
        