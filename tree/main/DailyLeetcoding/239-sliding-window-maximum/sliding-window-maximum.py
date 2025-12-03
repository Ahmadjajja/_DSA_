from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQ = deque()
        res = []

        for i in range(k - 1):
            while maxQ and nums[i] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[i])

        l = 0
        for r in range(k - 1, len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])

            res.append(maxQ[0])

            if nums[l] == maxQ[0]:
                maxQ.popleft()
            l += 1
        
        return res
            

# tc : O(n)
# sc : O(n)
