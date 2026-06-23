class Solution:
    def singleNumber(self, n: list[int]) -> int:
        b=set(n)
        c=sum(b)
        
        a=sum(n)
        return (c*2-a)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r=0
        for i in nums:
            r^=i
        return r

"""