class Solution(object):
    def letterCombinations(self, di):
        if not di:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans=[]
        def dfs(i,cur):
            if i==len(di):
                ans.append(cur)
                return
            for  c in d[di[i]]:
                dfs(i+1,cur+c)
        dfs(0,"")
        return ans
        