class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longSubStr = 0
        uniqueCh = set()

        l, r = 0, 0
        while l <= r and r < len(s):
            while s[r] in uniqueCh:
                leftElem = s[l]
                uniqueCh.remove(leftElem)
                l += 1
            uniqueCh.add(s[r])
            r += 1
            longSubStr = max(longSubStr, r - l)
        
        return longSubStr