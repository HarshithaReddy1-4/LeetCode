class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        while k > 0:
            for i in range(n):
                temp = grid[i][m - 1]
                for j in range(m - 1, 0, -1):
                    grid[i][j] = grid[i][j -  1]
                grid[i][0] = temp
            temp = grid[n - 1][0]
            for i in range(n - 1, 0, -1):
                grid[i][0] = grid[i - 1][0]
            grid[0][0] = temp
            k -= 1
        
        return grid
        
