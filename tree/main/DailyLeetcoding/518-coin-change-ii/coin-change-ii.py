class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(index, curAmount):
            if curAmount == amount:
                return 1
            if curAmount > amount or index >= len(coins):
                return 0

            if (index, curAmount) in cache:
                return cache[(index, curAmount)]

            # add curAmount
            left = dfs(index, curAmount + coins[index])
            # skip curAmount
            right = dfs(index + 1, curAmount)

            cache[(index, curAmount)] = left + right
            
            return cache[(index, curAmount)]

        return dfs(0, 0)


        