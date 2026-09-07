class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(index1, index2):
            if index1 == len(s1) and index2 == len(s2):
                return True
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            ans = False
            if index1 < len(s1) and s1[index1] == s3[index1 + index2]:
                ans = ans or dfs(index1 + 1, index2)
            if index2 < len(s2) and s2[index2] == s3[index1 + index2]:
                ans = ans or dfs(index1, index2 + 1)

            cache[(index1, index2)] = ans
            return ans

        return dfs(0, 0)