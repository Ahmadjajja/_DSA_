class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            cur = intervals[i]
            if cur[1] < newInterval[0]:
                res.append(cur)
            elif cur[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                s = min(cur[0], newInterval[0])
                e = max(cur[1], newInterval[1])
                newInterval = [s, e]
        
        res.append(newInterval)
        return res

        