class Solution:
    def searchInsert(self, n: list[int], t: int) -> int:
        l=0
        h=len(n)-1
        
        while(l<=h):
            mid=(l+h)//2
            if(n[mid]==t):
                return mid
            elif(n[mid]>t):
                h=mid-1
            else:
                l=mid+1
    
        return l