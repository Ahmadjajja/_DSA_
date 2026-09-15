import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        # Impossible if any character needs to appear more than half the slots
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Max-heap of (-count, char)
        max_heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        prev = None  # (count, char) of the character we just placed, on cooldown

        while max_heap:
            count, ch = heapq.heappop(max_heap)
            result.append(ch)

            # Release the previous char from cooldown, now that a step has passed
            if prev:
                heapq.heappush(max_heap, prev)

            # This char goes on cooldown for one step (count + 1 since it's negative)
            prev = (count + 1, ch) if count + 1 != 0 else None

        return ''.join(result)