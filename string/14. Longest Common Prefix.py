class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""    
        fd = strs[0]
        for i in range(len(fd)):
            char = fd[i]
            for od in strs[1:]:
                if i == len(od) or od[i] != char:
                    return fd[:i]
        return fd