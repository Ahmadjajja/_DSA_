from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        total = 0
        for n in nums:
            total += n

        if total % 2 == 1:
            return False

        target = total // 2

        memo = {}  # (index, current_sum) -> bool

        def dfs(index: int, cSum: int) -> bool:
            if cSum == target:
                return True
            if index == len(nums) or cSum > target:
                return False
            key = (index, cSum)
            if key in memo:
                return memo[key]

            # choose or skip
            res = dfs(index + 1, cSum + nums[index]) or dfs(index + 1, cSum)
            memo[key] = res
            return res

        # Optional prune: try bigger numbers first to hit target faster
        nums.sort(reverse=True)

        return dfs(0, 0)
