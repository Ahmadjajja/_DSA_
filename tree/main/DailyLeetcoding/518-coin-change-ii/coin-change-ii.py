class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in range(len(coins) - 1, -1, -1):
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1

            for a in range(1, amount + 1):
                next_dp[a] = dp[a] 
                if a - coins[c] >= 0:
                    next_dp[a] += next_dp[a - coins[c]]
            dp = next_dp
        return next_dp[amount]
            

        # top down 
        # cache = {}

        # def dfs(index, curAmount):
        #     if curAmount == amount:
        #         return 1
        #     if curAmount > amount or index >= len(coins):
        #         return 0

        #     if (index, curAmount) in cache:
        #         return cache[(index, curAmount)]

        #     # add curAmount
        #     left = dfs(index, curAmount + coins[index])
        #     # skip curAmount
        #     right = dfs(index + 1, curAmount)

        #     cache[(index, curAmount)] = left + right

        #     return cache[(index, curAmount)]

        # return dfs(0, 0)

        # # tc -> O(n * m)
        # # sc -> O(n * m)


        