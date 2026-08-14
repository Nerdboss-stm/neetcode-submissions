class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if not (0<=r<rows and 0<=c<cols) or board[r][c]!="O":
                return
            board[r][c] = "T"
            for dr,dc in directions:
                dfs(r+dr, c+dc)
        
        for i in range(rows):
            for j in range(cols):
                if i in (0, rows - 1) or j in (0, cols - 1):
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

        