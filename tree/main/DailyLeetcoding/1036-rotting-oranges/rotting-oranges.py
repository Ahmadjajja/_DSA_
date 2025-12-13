class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # put all rotten oranges positions in q
        q = deque()
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0

        
        # multi sourse bfs
        lvl = 0
        dirArr = [[0, -1], [-1, 0], [0, 1], [1, 0]] # left, top, right, bottom
        

        while q:
            qSize = len(q)
            for i in range(qSize):
                cr, cc = q.popleft()
                for r,c in dirArr:
                    nr, nc = cr + r, cc + c

                    if 0 <= nr and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        freshOranges -= 1

            lvl += 1
            if freshOranges == 0:
                break
        
        if freshOranges > 0:
            return -1
        
        return lvl


# tc : O(m * n)
# sc : O(m * n)