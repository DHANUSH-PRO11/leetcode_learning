class Solution:
    def reverseWords(self, s: str) -> str:
        n=list(map(str,s.strip().split()))
        
        n.reverse()
        r = " ".join(n)
        return (r)
            