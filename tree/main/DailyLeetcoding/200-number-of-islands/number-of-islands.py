class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        dirArr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isIsland(row, col):
            visit.add((row, col))
            for r, c in dirArr:
                nr, nc = row + r, col + c
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visit or grid[nr][nc] == '0':
                    continue
                isIsland(nr, nc)

        no_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) in visit or grid[r][c] == '0':
                    continue
                isIsland(r, c)
                no_of_islands += 1
        
        return no_of_islands 




