class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num, lvl, intPart):
            if num == 0:
                return intPart
            
            if (num, lvl) in memo:
                return memo[(num, lvl)] * intPart
            pro = 1
            for i in range(1, num + 1):
                if i == n:
                    continue
                pro = max(pro, dfs(num - i, lvl + 1, i))
            
            memo[(num, lvl)] = pro

            return pro * intPart

        return dfs(n, 0, 1)
        