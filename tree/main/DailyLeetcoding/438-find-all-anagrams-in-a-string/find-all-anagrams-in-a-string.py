class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pf = Counter(p)
        sf = {}
        res = []

        l = 0

        for r in range(len(s)):
            ch = s[r]

            if ch in pf:
                sf[ch] = sf.get(ch, 0) + 1
                while sf[ch] > pf[ch]:
                    sf[s[l]] -= 1
                    l += 1
                if (r - l + 1) == len(p):
                    res.append(l)
                    sf[s[l]] -= 1
                    l += 1
            else:
                sf.clear()
                l = r + 1
        
        return res
            



        