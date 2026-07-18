class Solution:
    def insert(self, inte: list[list[int]], n: list[int]) -> list[list[int]]:
        inte.append(n)
        inte.sort()
        s,e=inte[0]
        an=[]
        for se,en in inte[1:]:
            if se <=e:
                e=max(e,en)
            else:
                an.append([s,e])
                s,e=se,en
        an.append([s,e])
        return an

