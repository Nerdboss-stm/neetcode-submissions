class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                

        while q:
            qlen = len(q)
            for _ in range(qlen):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>= cols:
                        continue
                    if grid[nr][nc] != 2147483647:
                        continue
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
        
