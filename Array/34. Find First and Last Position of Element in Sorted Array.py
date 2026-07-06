class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if(target in nums):
            d=nums.count(target)
            a=nums.index(target)
            if d==a:
                b=a
            else:
                b=a+d-1
            print(d,a,b)
            return [a,b]
        else:
            return [-1,-1]        