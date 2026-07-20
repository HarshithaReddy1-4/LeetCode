class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if visited[i][j] == 1:
                return
            if grid[i][j] == '0':
                return
            visited[i][j] = 1
            for ni, nj in directions:
                dfs(i + ni, j + nj)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)
        
        return count
