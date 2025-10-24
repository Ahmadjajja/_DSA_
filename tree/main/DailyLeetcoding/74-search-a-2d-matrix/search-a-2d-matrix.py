class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find target row
        up, bot = 0, len(matrix) - 1
        row = -1
        while up <= bot:
            mid = (up + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                up = mid + 1
            else:
                row = mid
                break
        
        print("row -> ", row)

        # find target in that row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else: 
                l = mid + 1
        
        return False

        