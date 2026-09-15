class Solution:
    def reorganizeString(self, s: str) -> str:
        freqList = {}
        for ch in s:
            freqList[ch] = freqList.get(ch, 0) + 1
        res = ""
        maxH = []
        cooldownElem = (0, 'A')
        for key, val in freqList.items():
            heapq.heappush(maxH, (-val, key))
        for i in range(len(s)):
            if maxH and maxH[0][1] != cooldownElem[1]:
                popedElem = heapq.heappop(maxH)
                res += popedElem[1]
                if cooldownElem[0] != 0:
                    heapq.heappush(maxH, cooldownElem)
                cooldownElem = (popedElem[0] + 1, popedElem[1])
            else:
                return ""
        return res
