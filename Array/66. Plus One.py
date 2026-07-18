class Solution:
    def plusOne(self, t: list[int]) -> list[int]:
        s=""
        for i in t:
            s+=str(i)
        a=int(s)+1
        d=str(a)
        m=[]
        for i in d:
            m.append(int(i))
        
        return m