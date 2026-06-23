class Solution:
    def findNumbers(self, n: list[int]) -> int:
        return sum(len(str(i))%2==0 for i in n)