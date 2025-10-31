class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(index, curSum, curCum):

            if curSum == target:
                res.append(curCum)
                return

            if index >= len(candidates) or curSum > target:
                return

            for i in range(index, len(candidates)):
                dfs(i, curSum + candidates[i], curCum + [candidates[i]])

            return

        dfs(0, 0, [])

        return res
        

        
        