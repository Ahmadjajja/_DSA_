class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resP = []
        visit = set()

        def dfs(p):
            if len(p) == len(nums):
                resP.append(p.copy())
                return
            

            for i in range(len(nums)):
                if i in visit:
                    continue
                
                visit.add(i)
                p.append(nums[i])
                dfs(p)
                visit.remove(i)
                p.pop()
        
        dfs([])

        return resP

        