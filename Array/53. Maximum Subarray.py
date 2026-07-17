class Solution:
    def maxSubArray(self, n: list[int]) -> int:
        c=n[0]
        s=n[0]
        for i in n[1:]:
            c=max(i,c+i)
            s=max(c,s)
        return s