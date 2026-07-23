class Solution:
    def threeSum(self, n: list[int]) -> list[list[int]]:
        n.sort()
        
        a=[]
        for i in range(len(n)):
            if i>0 and n[i]==n[i-1]:
                continue
            l=i+1
            r=len(n)-1
            while(l<r):
                s=n[i]+n[l]+n[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    a.append([n[i],n[l],n[r]])
                    l+=1
                    r-=1
                    while l<r and n[l]==n[l-1]:
                        l+=1
        return a

        