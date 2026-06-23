class Solution:
    def numberOfEmployeesWhoMetTarget(self, h: list[int], t: int) -> int:
        return sum(i>=t for  i in h)