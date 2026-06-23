class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl= ""

        for c in s:
            if c.isalnum():
                cl+= c.lower()

        return cl== cl[::-1]