class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dirArr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # base case
            for row, col in dirArr:
                nr, nc = r + row, c + col

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == '0':
                    continue
                
                visited.add((nr, nc))
                dfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited or grid[row][col] == '0':
                    continue
                visited.add((row, col))
                dfs(row, col)
                islands += 1
        
        return islands




        

        