class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(sum):
            if sum > amount:
                return float("inf")
            if sum == amount:
                return 0
            if sum in cache:
                return cache[sum]

            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, dfs(sum + coin))
            
            cache[sum] = 1 + minCoins 

            return cache[sum]
        ans = dfs(0)
        return ans if ans != float('inf') else -1
