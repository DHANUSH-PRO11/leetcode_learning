class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def backt(cur,open ,close):
            if len(cur)==2*n:
                ans.append(cur)
                return
            if open<n:
                backt(cur+"(",open+1,close)
            if close<open:
                backt(cur+")",open,1+close)
        backt("",0,0)
        return ans