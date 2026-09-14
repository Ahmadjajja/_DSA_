class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                cache[(i, j)] = dfs(i + 1, j - 1) + 2
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))

            return cache[(i, j)]

        return dfs(0, len(s) - 1)