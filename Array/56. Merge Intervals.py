class Solution:
    def merge(self, inte: list[list[int]]) -> list[list[int]]:
        inte.sort()
        s,e=inte[0]
        an=[]
        for sr,en in inte[1:]:
            if sr<=e:
                e=max(e,en)
            else:
                an.append([s,e])
                s,e=sr,en
        an.append([s,e])
        return an