class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        se=set()
        an=set()
        for i in range(len(s)-9):
            sub=s[i:i+10]
            if sub in se:
                an.add(sub)
            else:
                se.add(sub)
        return list(an)