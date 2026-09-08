class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][buying]: i ranges 0..n+1 to safely cover i+2 lookups
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                cooldown = dp[i + 1][buying]
                if buying:
                    buy = dp[i + 1][not buying] - prices[i]
                    dp[i][buying] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][not buying] + prices[i]
                    dp[i][buying] = max(sell, cooldown)

        return dp[0][True]

        # tc -> O(n)
        # sc -> O(n)