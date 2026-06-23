class Solution:
    def shortestToChar(self, s, c):
        pos = []

        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)

        ans = []

        for i in range(len(s)):
            ans.append(min(abs(i - p) for p in pos))

        return ans