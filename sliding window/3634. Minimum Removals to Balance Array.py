class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        l=0
        maxx=0
        n=len(nums)
        for r in range(n):
            while(nums[r]>nums[l]*k):
                l+=1
            maxx=max(maxx,r-l+1)
        return n-maxx
      