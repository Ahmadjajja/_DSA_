class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_square = 0

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                    max_square = max(max_square, dp[r][c])

        return max_square * max_square