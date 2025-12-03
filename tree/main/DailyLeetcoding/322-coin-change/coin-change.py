class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            if amount in memo:
                return memo[amount]
            
            minCoins = float("inf")
            for coin in coins:
                minCoins = min(minCoins, dfs(amount - coin) + 1)
            
            memo[amount] = minCoins
            return memo[amount] 

        ans = dfs(amount)
        print("memo : ", memo)
        return ans if ans != float('inf') else -1
        