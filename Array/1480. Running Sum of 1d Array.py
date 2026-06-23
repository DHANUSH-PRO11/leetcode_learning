class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s=[]
        a=0
        for i in nums:
            a+=i
            s.append(a)
        return(s)