class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        a=0
        b=0
        for i in nums:
            if i==1:
                a+=1
                b=max(a,b)
            else:
                a=0
            
        return b