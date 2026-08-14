class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            for dr, dc in ((0,1), (0,-1), (1,0),(-1,0)):
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)
        return count
                
                            
                            