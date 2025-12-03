from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque() # monotonic ascending order
        maxQ = deque() # monotonic descending order
        res = 0
        l = 0

        for r in range(len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            
            maxQ.append(nums[r])
            minQ.append(nums[r])

            while maxQ and minQ and maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1
            
            res = max(res, r - l + 1)
        
        return res