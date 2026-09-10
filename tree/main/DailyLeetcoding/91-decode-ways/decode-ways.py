class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == '0' or index > len(s):
                return 0

            if index in cache:
                return cache[index]
            
            left = dfs(index + 1)
            right = 0
            if index + 2 <= len(s) and int(s[index: index + 2]) < 27:
                right = dfs(index + 2)
            cache[index] = left + right
            return cache[index]
        
        return dfs(0)
            
        