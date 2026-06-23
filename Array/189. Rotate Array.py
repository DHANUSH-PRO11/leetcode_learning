class Solution:
    def rotate(self, n: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(n)
        k%=a
        n.reverse()
        n[:k]=reversed(n[:k])
        n[k:]=reversed(n[k:])