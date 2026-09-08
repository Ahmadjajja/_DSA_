class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]

        # tc -> O(n)
        # sc -> O(n)


        # cache = {}
        # def dfs(i, res):
        #     if i == len(nums):
        #         if res == target:
        #             return 1
        #         else:
        #             return 0
            
        #     if (i, res) in cache:
        #         return cache[(i, res)]
            
        #     left = dfs(i + 1, res - nums[i])
        #     right = dfs(i + 1, res + nums[i])

        #     cache[(i, res)] = left + right
            
        #     return cache[(i, res)]

        # return dfs(0, 0)

        # # tc -> O(n)
        # # sc -> O(n)
        