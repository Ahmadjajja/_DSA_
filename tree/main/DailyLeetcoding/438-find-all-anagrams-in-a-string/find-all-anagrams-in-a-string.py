class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount = [0] * 26
        sCount = [0] * 26

        for ch in p:
            pCount[ord(ch) - ord('a')] += 1

        res = []
        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                sCount[ord(s[i - len(p)]) - ord('a')] -= 1

            if sCount == pCount:
                res.append(i - len(p) + 1)

        return res