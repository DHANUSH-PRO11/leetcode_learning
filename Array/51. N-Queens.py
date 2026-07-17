class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        res = []
        
        def dfs(r, cols, diag1, diag2, path):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in path])
                return
            for c in range(n):
                if c not in cols and r - c not in diag1 and r + c not in diag2:
                    dfs(r + 1, cols | {c}, diag1 | {r - c}, diag2 | {r + c}, path + [c])

        dfs(0, set(), set(), set(), [])
        return res