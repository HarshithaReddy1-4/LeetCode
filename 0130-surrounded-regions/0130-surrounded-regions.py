class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        def dfs(i, j):
            board[i][j] = 'Z'
            for ni, nj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newi, newj = i + ni, j + nj
                if newi < 0 or newj < 0 or newi >= m or newj >= n or board[newi][newj] != 'O':
                    continue
                dfs(newi, newj)

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)

        for j in [0, n - 1]:
            for i in range(1, m - 1):
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Z':
                    board[i][j] = 'O'

        