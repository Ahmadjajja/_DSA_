class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        output = []
        l = r = 0

        while r < len(nums):
            # pop smaller value from the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove left val from window 
            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output