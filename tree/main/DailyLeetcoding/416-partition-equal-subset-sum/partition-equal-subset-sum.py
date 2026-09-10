class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        cache = {}
        def dfs(curIndex, remaining):
            if remaining == 0:
                return True
            if remaining < 0 or curIndex == len(nums):
                return False
            if (curIndex, remaining) in cache:
                return cache[(curIndex, remaining)]

            # either skip nums[curIndex] or include it
            result = dfs(curIndex + 1, remaining) or dfs(curIndex + 1, remaining - nums[curIndex])

            cache[(curIndex, remaining)] = result
            return result

        return dfs(0, target)