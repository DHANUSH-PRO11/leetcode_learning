class Solution:
    def numOfSubarrays(self, a: list[int], k: int, t: int) -> int:
        c,se=0,sum(a[:k])
        if se//k>=t:
            c+=1
        for  i in range(k,len(a)):
            se+=a[i]-a[i-k]
            if se//k>=t:
                c+=1
        return c 
