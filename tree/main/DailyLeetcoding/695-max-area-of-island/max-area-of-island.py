class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        dirArr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            visit.add((r, c))

            count_no_of_cells = 0
            for dr, dc in dirArr:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visit or grid[nr][nc] == 0:
                    continue
                
                count_no_of_cells += dfs(nr, nc)
            
            return 1 + count_no_of_cells

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] != 0:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea