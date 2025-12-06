class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0  # farthest index we can reach so far

        for i in range(len(nums)):
            # if we are standing on an index we can't reach
            if i > maxReach:
                return False

            # update farthest reachable index
            maxReach = max(maxReach, i + nums[i])

            # if we can reach or pass the last index
            if maxReach >= len(nums) - 1:
                return True

        return True  # if loop finishes, last index is reachable
