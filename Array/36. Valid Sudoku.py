class Solution:
    def isValidSudoku(self, b: list[list[str]]) -> bool:
        r=[set() for i in range(9)]
        c=[set() for i in range(9)]
        b=[set() for i in range(9)]
        for  i in range(9):
            for j in range(9):
                n=b[i][j]
                if n ==".":
                    continue
                bo = (i//3)*3+(j/3)
                if n in r[i] or n in c[j] or n in b[bo]:
                    return False
                r[i].add(n)
                c[j].add(n)
                b[bo].add(n)
        return True