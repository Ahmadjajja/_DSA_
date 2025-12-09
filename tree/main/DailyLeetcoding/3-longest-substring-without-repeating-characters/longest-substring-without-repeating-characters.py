class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hm = {}

        l = 0
        for r in range(len(s)):

            while s[r] in hm and hm[s[r]] >= l:
                l = hm[s[r]] + 1
            
            hm[s[r]] = r
            res = max(res,r - l + 1)

        return res
        