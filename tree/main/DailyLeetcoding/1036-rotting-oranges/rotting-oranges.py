class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        dirArr = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        time = 0
        unRottenOranges = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    unRottenOranges += 1

        while q:
            qSize = len(q)
            rotted = False
            for i in range(qSize):
                r, c = q.popleft()
                for dr, dc in dirArr:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    unRottenOranges -= 1
                    q.append((nr, nc))
                    rotted = True
            if rotted:
                time += 1

        return -1 if unRottenOranges != 0 else time