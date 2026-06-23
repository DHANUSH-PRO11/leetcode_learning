class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        a=nums.count(val)
        for i in range(a):
            nums.remove(val)
       