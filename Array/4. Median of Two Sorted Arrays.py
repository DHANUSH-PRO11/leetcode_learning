class Solution(object):
    def findMedianSortedArrays(self, n, m):
        n.extend(m)
        n.sort()
        o=int(len(n))
        if len(n)%2!=0:
            return float(n[o/2])
        else:
            return float((n[o/2]+n[(o-1)/2]))/2