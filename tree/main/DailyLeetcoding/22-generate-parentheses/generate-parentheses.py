class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(index, s, open, close):
            if close > open or open > n or close > n:
                return

            if index == n * 2:
                res.append(s)
                return 
            
            dfs(index + 1, s + "(", open + 1, close)
            dfs(index + 1, s + ")", open, close + 1)

        dfs(0, "", 0, 0)

        return res


