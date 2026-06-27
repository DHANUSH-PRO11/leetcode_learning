from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        c = Counter(nums)
        ans = 0

        for x in c:
            if x + 1 in c:
                ans = max(ans, c[x] + c[x + 1])

        return ans