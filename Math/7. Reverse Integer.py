class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        a=''
        if s[0]=='-':
            a='-'+s[:0:-1]
        else:
            a=s[::-1]
        n=int(a)
        if n < -2**31 or n > 2**31 - 1:
            return 0
        return n