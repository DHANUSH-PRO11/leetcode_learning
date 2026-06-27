from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        s = 0
        ans = 0

        for right in range(len(nums)):
            s += nums[right]
            freq[nums[right]] += 1

            if right - left + 1 > k:
                s -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, s)

        return ans