class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3) or len(s1) + len(s2) < len(s3):
            return False

        memo = {}

        def dfs(i1, i2, i3, st):
            if i1 >= len(s1) and i2 >= len(s2):
                return st == s3
            
            if i1 < len(s1) and s3[i3] != s1[i1] and i2 < len(s2) and s3[i3] != s2[i2]:
                return False
            
            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]

            left = False
            if i1 < len(s1) and s3[i3] == s1[i1]:
                left = dfs(i1 + 1, i2, i3 + 1, st + s3[i3])
            right = False
            if i2 < len(s2) and s3[i3] == s2[i2]:
                right = dfs(i1, i2 + 1, i3 + 1, st + s3[i3])
            
            memo[(i1, i2, i3)] = left or right
            
            return left or right

        return dfs(0, 0, 0, "")

        