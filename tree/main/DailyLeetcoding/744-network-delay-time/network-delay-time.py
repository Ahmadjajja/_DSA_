class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for s, t, w in times:
            adjList[s].append((t, w))
        minT = 0
        visitSet = set()
        minHeap = [(0, k)]
        while minHeap:
            w1, curNode = heapq.heappop(minHeap)
            if curNode in visitSet:
                continue
            visitSet.add(curNode)
            minT = max(minT, w1)
            for neiNode, w2 in adjList[curNode]:
                if neiNode not in visitSet:
                    heapq.heappush(minHeap, (w1 + w2, neiNode))

        return minT if len(visitSet) == n else -1

        