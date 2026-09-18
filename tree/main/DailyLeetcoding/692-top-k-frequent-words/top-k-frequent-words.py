from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        freq = Counter(words)
        maxH = [[-count, word] for word, count in freq.items()]
        heapq.heapify(maxH)

        return [heapq.heappop(maxH)[1] for _ in range(k)]
