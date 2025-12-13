class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

    # pick a window and try finding the maximum freq element
    # upper case english letters -> 26

        freqArr = [0] * 26

        l = 0

        res = float("-inf")

        for r in range(len(s)):
            ch = s[r]
            chIndex = ord(ch) - ord("A")
            freqArr[chIndex] += 1
            maxCount = max(freqArr)
            misMatch = (r - l + 1) - maxCount
            if misMatch <= k:
                res = max(res, (r - l + 1))
                continue
            

            while not (misMatch <= k):
                ch = s[l]
                chIndex = ord(ch) - ord("A")
                freqArr[chIndex] -= 1
                l += 1
                maxCount = max(freqArr)
                misMatch = (r - l + 1) - maxCount
            
        return res


# tc -> O(n + 26 + constant time) -> O(n)
# sc -> O(26) -> O(1)
