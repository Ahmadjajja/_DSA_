class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        matrix = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(matrix)):
            matrix[i][0] = i
        for i in range(len(matrix[0])):
            matrix[0][i] = i

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if word2[i - 1] == word1[j - 1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(
                        matrix[i-1][j],    # Deletion
                        matrix[i][j-1],    # Insertion
                        matrix[i-1][j-1]   # Substitution
                    )        
        return matrix[len(matrix) - 1][len(matrix[0]) - 1]