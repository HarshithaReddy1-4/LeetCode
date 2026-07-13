class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3) * 3 + (j // 3)].add(board[i][j])
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        block = (i//3) * 3 + (j // 3)
                        for ch in '123456789':
                            if ch not in rows[i] and ch not in cols[j] and ch not in blocks[block]:
                                board[i][j] = ch
                                rows[i].add(ch)
                                cols[j].add(ch)
                                blocks[block].add(ch)

                                if solve():
                                    return True
                                
                                board[i][j] = '.'
                                rows[i].discard(ch)
                                cols[j].discard(ch)
                                blocks[block].discard(ch)
                        return False
            return True
        solve()
                                

