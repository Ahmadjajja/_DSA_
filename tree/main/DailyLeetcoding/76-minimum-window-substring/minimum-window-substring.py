class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        res, resLen = [-1, -1], float('inf')
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1] + 1] if resLen != float('inf') else ""




        