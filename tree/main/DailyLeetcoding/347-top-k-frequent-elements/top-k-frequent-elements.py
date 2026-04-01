import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        maxheap = []
        for key, val in freq.items():
            heapq.heappush(maxheap, (-val, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(maxheap)[1])

        return res

        # tc -> O(n) + O(mlogm) + O(klogm)
        # sc -> O(m)