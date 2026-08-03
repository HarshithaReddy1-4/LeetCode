class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = 0
        while q and fresh > 0:
            minutes += 1

            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj  < n and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        q.append((ni, nj))

        return minutes if fresh == 0 else  -1
        
