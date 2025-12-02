class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 0, 1

        for i in range(n):
            print(i)
            s = first + second
            first = second
            second = s
        
        return second



        # # top-down approach
        # memo = {}
        # def dfs(steps):
        #     if steps == n:
        #         return 1
        #     if steps > n:
        #         return 0
            
        #     if steps in memo:
        #         return memo[steps]

        #     left = dfs(steps + 1)
        #     right = dfs(steps + 2)

        #     memo[steps] = left + right

        #     return memo[steps]
        
        # return dfs(0)

# tc: O(n)
# sc: O(n)

        