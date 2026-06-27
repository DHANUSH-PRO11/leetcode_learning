from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n=len(p)

        c1=Counter(p)
        c2=Counter(s[:n])
        an=[]
        if c1 == c2:
            an.append(0)
        for i in range(n,len(s)):
            c2[s[i]]+=1
            c2[s[i-n]]-=1
            if c2[s[i-n]]==0:
                del c2[s[i-n]]
            if  c1==c2:
                an.append(i-n+1)
        return an