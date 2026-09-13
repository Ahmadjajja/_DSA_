class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        minH = []
        i = 0
        n = len(events)
        countConf = 0

        for day in range(1, (10**5) + 1):
            # gather all the days which are starting at current day
            while i < n and events[i][0] <= day:
                heapq.heappush(minH, events[i][1])
                i += 1
            # discard if any window is expired
            while minH and minH[0] < day:
                heapq.heappop(minH)
            
            if minH:
                heapq.heappop(minH)
                countConf += 1
            
            if i == n and not minH:
                break
        
        return countConf