class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        visited = set() # this is gonna contain tuple (i, j)
        islands = 0
        dirArr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        # if rows == 1 and cols == 1:
        #     return grid[0][0] == "1"

        def dfs(r, c):

            visited.add((r, c))

            for dr, dc in dirArr:
                nr = r + dr
                nc = c + dc
                # checking out of range
                if nr >= rows or nr < 0 or nc >= cols or nc < 0 or grid[nr][nc] == "0" or (nr, nc) in visited:
                    continue
                
                dfs(nr, nc)



        for row in range(rows):
            for col in range(cols):

                cur = grid[row][col]
                if cur == "0" or (row, col) in visited:
                    continue
                else:

                    dfs(row, col)
                    islands += 1
        
        return islands

# tc => O()
# sc => O()




        