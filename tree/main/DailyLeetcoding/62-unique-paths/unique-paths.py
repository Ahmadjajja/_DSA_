class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[0] * n] * m

        print(matrix)
        matrix[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue

                currentVal = 0
                # check if top is valid
                if 0 <= row - 1 < m:
                    currentVal += matrix[row - 1][col]

                # check if left is valid
                if 0 <= col - 1 < n:
                    currentVal += matrix[row][col - 1]
                
                matrix[row][col] = currentVal


        return matrix[m - 1][n - 1]
        