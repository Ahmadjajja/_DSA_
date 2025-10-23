class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, rAmount):
            if rAmount == 0:
                return 1
            if i >= len(coins) or rAmount < 0:
                return 0
            
            if (i, rAmount) in memo:
                return memo[(i, rAmount)]
            
            # 2 choices: take current coin or skip
            take = dfs(i, rAmount - coins[i])
            skip = dfs(i + 1, rAmount)
            memo[(i, rAmount)] = take + skip
            return memo[(i, rAmount)]

        return dfs(0, amount)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo = {}

#         def dfs(index, rAmount):
#             if rAmount == 0:
#                 return 1
#             if rAmount < 0 or index >= len(coins):
#                 return 0
            
#             if (index, rAmount) in memo:
#                 return memo[(index, rAmount)]
#             ans = 0
#             for i in range(index, len(coins)):
#                 ans += dfs(index + 1, rAmount - coins[index])
            
#             memo[(index, rAmount)] = ans

#             return ans

#         return dfs(0, amount)
        