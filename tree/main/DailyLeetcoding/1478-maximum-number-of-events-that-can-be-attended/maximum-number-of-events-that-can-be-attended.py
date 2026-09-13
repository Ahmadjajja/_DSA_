class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[0])
        minH = []          # heap of end days for started, unattended events
        i, n = 0, len(events)
        countConf = 0

        for day in range(1, 10**5 + 1):
            # push all events that have started by today
            while i < n and events[i][0] <= day:
                heapq.heappush(minH, events[i][1])
                i += 1

            # drop events whose window has already closed
            while minH and minH[0] < day:
                heapq.heappop(minH)

            # attend whichever remaining event ends soonest
            if minH:
                heapq.heappop(minH)
                countConf += 1

            # if i == n and not minH:   # nothing left to process
            #     break

        return countConf