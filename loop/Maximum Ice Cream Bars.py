class Solution:
    def maxIceCream(self, c: list[int], co: int) -> int:
        c.sort()
        s=0
        
        for i in c:
            if co<i:
                break
            co-=i
            s+=1
        return s