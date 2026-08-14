class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        pqueue = deque()
        aqueue = deque()

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pqueue.append((i,j))

        for i in range(rows):
            for j in range(cols):
                if i == rows-1 or j == cols-1:
                    aqueue.append((i,j))
        
        def bfs(queue, seen):
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols:
                        continue
                    if not (heights[nr][nc] >= heights[r][c]):
                        continue
                    if (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    queue.append((nr, nc))
            return seen
        
        seen_p = set(pqueue)
        seen_a = set(aqueue)

        pacific = bfs(pqueue,seen_p)
        atlantic = bfs(aqueue,seen_a)

        return [list(cell) for cell in pacific & atlantic]