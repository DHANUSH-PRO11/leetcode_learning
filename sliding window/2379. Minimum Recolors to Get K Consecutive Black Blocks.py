class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        c=sum(i=="W" for i in b[:k])
        a=c
        for i in range(k,len(b)):
        
            if b[i]=="W":
                c+=1
            if b[i-k]=="W":
                c-=1

            a=min(a,c)

        return a
    
