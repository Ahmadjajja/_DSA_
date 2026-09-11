class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxH = [(-val, key) for key, val in freq.items()]
        heapq.heapify(maxH)
        res = []
        while k > 0:
            val, key = heapq.heappop(maxH)
            res.append(key)
            k -= 1
        
        return res

        