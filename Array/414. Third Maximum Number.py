class Solution:
    def thirdMax(self, n: list[int]) -> int:
        n=sorted(set(n),reverse =True)
        
        if len(n)>=3:
            return n[2]
       
        return n[0]