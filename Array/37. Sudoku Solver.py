class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + j//3].add(board[i][j])

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":

                        box = (i//3)*3 + j//3

                        for ch in "123456789":

                            if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box]:

                                board[i][j] = ch
                                rows[i].add(ch)
                                cols[j].add(ch)
                                boxes[box].add(ch)

                                if solve():
                                    return True

                                board[i][j] = "."
                                rows[i].remove(ch)
                                cols[j].remove(ch)
                                boxes[box].remove(ch)

                        return False
            return True

        solve()