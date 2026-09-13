class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] != 'O'
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, board[r][c])
            dfs(r - 1, c, board[r][c])
            dfs(r, c + 1, board[r][c])
            dfs(r, c - 1, board[r][c])

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c, board[0][c])
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c, board[ROWS - 1][c])

        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0, board[r][0])
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1, board[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'
        