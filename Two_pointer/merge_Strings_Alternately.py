class Solution:
    def mergeAlternately(self, w: str, e: str) -> str:
        a=''
        i=j=0
        while(i<len(w) and j<len(e)):
            a+=w[i]
            a+=e[j]
            i+=1
            j+=1
        while(i<len(w)):
            a+=w[i]
            i+=1
        while(j<len(e)):
            a+=e[j]
            j+=1
        return a