from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        d=defaultdict(int)
        ans=[-1,-1]
        minlen=float("inf")
        have=0
        required=len(need)
        l=0
        for r  in range(len(s)):
            ch=s[r]
            d[ch]+=1
            if ch in need and d[ch]==need[ch]:
                have+=1
            while have==required:
                if r-l+1<minlen:
                    minlen=r-l+1
                    ans=[l,r]
                d[s[l]]-=1
                if s[l] in need and d[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        l,r=ans
        return "" if minlen==float("inf") else s[l:r+1]