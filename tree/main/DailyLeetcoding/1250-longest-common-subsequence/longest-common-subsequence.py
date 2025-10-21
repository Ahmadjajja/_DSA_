class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        matrix = [[0]*(m+1) for _ in range(n+1)]  # independent rows

        for row in range(len(matrix)):
            if row == 0:
                continue
            for col in range(len(matrix[0])):
                if col == 0:
                    continue
                if text1[row - 1] == text2[col - 1]:
                    matrix[row][col] = matrix[row - 1][col - 1] + 1
                else:
                    matrix[row][col] = max(
                        matrix[row][col - 1], # prev
                        matrix[row - 1][col - 1], # diag
                        matrix[row - 1][col], # up
                    )

        print(matrix)

        return matrix[len(matrix) - 1][len(matrix[0]) - 1]






        