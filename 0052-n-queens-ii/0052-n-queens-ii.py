class Solution:
    def totalNQueens(self, n: int) -> int:
        rows, cols, posD, negD = set(), set(), set(), set()
        board = [['.'] * n for _ in range(n)]
        res = 0
        def bt(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if i in rows or j in cols or i + j in posD or i - j in negD or board[i][j] == 'Q':
                    continue
                board[i][j] = 'Q'
                rows.add(i)
                cols.add(j)
                posD.add(i + j)
                negD.add(i - j)
                bt(i + 1)
                board[i][j] = '.'
                rows.discard(i)
                cols.discard(j)
                posD.discard(i + j)
                negD.discard(i - j)
        bt(0)
        return res