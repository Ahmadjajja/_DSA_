class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # def mergeIntervals(intervals : List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevPair = res[-1]
            curPair = intervals[i]
            if prevPair[1] >= curPair[0]:
                res[-1][1] = max(prevPair[1], curPair[1])
            else:
                res.append(curPair)
        return res

        