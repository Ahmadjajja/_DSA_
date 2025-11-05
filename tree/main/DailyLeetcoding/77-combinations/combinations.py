class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []


        def dfs(index, cur):
            if len(cur) == k:
                res.append(cur)
                return
            if index >= n:
                return
            for i in range(index + 1, n):
                dfs(i, cur + [i + 1])

        for i in range(n):
            dfs(i, [i + 1])

        return res
        