class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        n = len(code)

        if k == 0:
            return [0] * n

        ans = [0] * n

        if k > 0:
            s = sum(code[1:k+1])

            for i in range(n):
                ans[i] = s
                s -= code[(i + 1) % n]
                s += code[(i + k + 1) % n]

        else:
            k = -k
            s = sum(code[n-k:])

            for i in range(n):
                ans[i] = s
                s -= code[(i - k + n) % n]
                s += code[i]

        return ans