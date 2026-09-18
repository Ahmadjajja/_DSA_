class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        maxH = []
        for key, val in freq.items():
            maxH.append((-val, key))

        heapq.heapify(maxH)
        res = []
        for _ in range(k):
            freq, val = heapq.heappop(maxH)
            res.append(val)
        return res


        # tc -> O(nlogn) + O(n) + O(u) + O(u) + O(klogu) -> O(nlogn)
        # sc -> O(u) + O(u) + O(k) -> O(n)

        