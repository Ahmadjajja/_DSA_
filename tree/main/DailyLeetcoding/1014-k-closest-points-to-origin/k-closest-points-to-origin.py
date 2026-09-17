import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x2, y2 = 0, 0 

        dist_list = [
            [math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), x1, y1]
            for x1, y1 in points
        ]

        heapq.heapify(dist_list)

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(dist_list)
            result.append([x, y])

        return result