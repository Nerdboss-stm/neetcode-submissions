class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()
        fresh =0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0
        while q and fresh:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols:
                        continue
                    if grid[nr][nc]!=1:
                        continue
                    grid[nr][nc]=2
                    fresh -= 1
                    q.append((nr,nc))
            minutes+=1
        
        return minutes if fresh == 0 else -1
        
