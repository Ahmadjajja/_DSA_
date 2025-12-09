class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in last and last[s[r]] >= l:
                l = last[s[r]] + 1

            last[s[r]] = r
            res = max(res, r - l + 1)

        return res
