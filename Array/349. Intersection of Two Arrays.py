class Solution:
    def intersection(self, n1: list[int], n2: list[int]) -> list[int]:
    
        return list(set(n1)&set(n2))
        