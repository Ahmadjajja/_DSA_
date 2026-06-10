class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        dirArr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):

            visited.add((row, col))
            size = 1
            for cr, cc in dirArr:
                nr, nc = row + cr, col + cc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0 or (nr, nc) in visited:
                    continue
                
                size += dfs(nr, nc)
            return size



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                
                res = max(res, dfs(r, c))
        
        return res

# tc => O(n * m)
# sc => O(n * m)
                
        