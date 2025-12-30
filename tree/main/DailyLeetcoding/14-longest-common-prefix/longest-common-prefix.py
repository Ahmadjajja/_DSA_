class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 2
        # flower

        firstWord = strs[0]
        res = 0
        for r in range(len(firstWord)):
            preFix = firstWord[0: r + 1]
            for s in strs:
                if preFix != s[0: r + 1]:
                    return firstWord[0: res]
            res += 1
        
        return firstWord[0: res]




        