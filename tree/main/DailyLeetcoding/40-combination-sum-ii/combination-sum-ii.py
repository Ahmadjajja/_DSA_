class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []


        def dfs(i, c, s):
            if s == target:
                combinations.append(c.copy())
                return
            if i == len(candidates) or s > target:
                return 
            

            dfs(i + 1, c + [candidates[i]], s + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i + 1, c, s)

        dfs(0, [], 0)

        return combinations
