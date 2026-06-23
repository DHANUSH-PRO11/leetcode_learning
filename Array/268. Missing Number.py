class Solution:
    def missingNumber(self, n: list[int]) -> int:
        m=len(n)
        return int(m*(m+1)/2)-sum(n)