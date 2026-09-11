class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        starts, ends = [], []
        for c, src, dst in trips:
            starts.append((src, c))
            ends.append((dst, c))
        
        curCap = 0
        conflictCount = 0
        starts.sort()
        ends.sort()
        
        s, e = 0, 0
        
        while s < len(trips):
            if starts[s][0] < ends[e][0]:
                curCap += starts[s][1]
                conflictCount += 1
                s += 1
            else:
                curCap -= ends[e][1]
                conflictCount -= 1
                e += 1
            if curCap > cap:
                return False
        return True

        