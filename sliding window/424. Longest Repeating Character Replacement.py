
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=defaultdict(int)
        l=ma=a=0
        for r in range(len(s)):
            d[s[r]]+=1
            ma=max(ma,d[s[r]])
            while((r-l+1)-ma>k):
                d[s[l]]-=1
                l+=1
            a=max(a,r-l+1)
        return a