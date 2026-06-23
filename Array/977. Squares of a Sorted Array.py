class Solution(object):
    def sortedSquares(self, n):
        
        
        a=[]
        for  i in n:
            a.append(i*i)
        a.sort()
        return a