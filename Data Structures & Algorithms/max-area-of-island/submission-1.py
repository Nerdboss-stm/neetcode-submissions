class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        best = 0

        def dfs(r,c):
            if not (0<=r<rows and 0<=c<cols) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + (dfs(r + 1, c) + dfs(r - 1, c)
                        + dfs(r, c + 1) + dfs(r, c - 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, dfs(i,j))
        return best

        