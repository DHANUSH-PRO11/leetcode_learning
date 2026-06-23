class Solution:
    def maximumWealth(self, a: list[list[int]]) -> int:
        q=[]
        for i in a:
            q.append(sum(i))
        return max(q)