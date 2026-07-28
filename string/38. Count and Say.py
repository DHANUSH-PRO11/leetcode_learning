class Solution:
    def countAndSay(self, n: int) -> str:

        ans = "1"

        for _ in range(n - 1):

            curr = []
            count = 1

            for i in range(1, len(ans)):

                if ans[i] == ans[i - 1]:
                    count += 1
                else:
                    curr.append(str(count))
                    curr.append(ans[i - 1])
                    count = 1

            curr.append(str(count))
            curr.append(ans[-1])

            ans = "".join(curr)

        return ans