class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, sum, com):

            # break point
            if sum == target:
                res.append(com)
                return
            if sum > target: 
                return
            
            for i in range(index, len(candidates)):
                dfs(i, sum + candidates[i], com + [candidates[i]])

        
        dfs(0, 0, [])
        return res
        