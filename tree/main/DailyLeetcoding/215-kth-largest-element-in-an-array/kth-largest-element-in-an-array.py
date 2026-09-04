class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)       # minHeap size becomes at most k+1
            if len(minHeap) > k:
                heapq.heappop(minHeap)          # shrink back down to k
        return minHeap[0] 
        