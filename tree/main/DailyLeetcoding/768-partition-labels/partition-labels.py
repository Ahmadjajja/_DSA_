class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        curFreq = {}
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            curFreq[s[i]] = curFreq.get(s[i], 0) + 1
            valid_partition = True
            for key, val in curFreq.items():
                if val != freq[key]:
                    valid_partition = False
                    break
            if valid_partition:
                res.append(r - l + 1)
                l = i + 1
                curFreq = {}
            r += 1
            
        return res
