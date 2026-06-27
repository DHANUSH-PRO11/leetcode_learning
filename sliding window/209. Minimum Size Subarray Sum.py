class Solution:
    def minSubArrayLen(self, t: int, n: list[int]) -> int:
        l=0
        s=0
        ans=float('inf')
        for r  in range(len(n)):
            s+=n[r]
            while s>=t:
                ans=min(ans,r-l+1)
                s-=n[l]
                l+=1
        return 0 if ans==float('inf') else ans
