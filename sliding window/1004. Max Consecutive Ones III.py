class Solution:
    def longestOnes(self, n: list[int], k: int) -> int:
        l=r=z=mx=0
        while(r<len(n)):
            if n[r]==0:
                z+=1
            while(z>k):
                if n[l]==0:
                    z-=1
                l+=1
            if (z<=k):
                mx=max(mx,r-l+1)
                r+=1
        return mx