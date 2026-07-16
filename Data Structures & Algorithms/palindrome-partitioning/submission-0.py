class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def ispalindrome(sub):
            return sub==sub[::-1]
        def backtrack(start,path):
            if start==len(s):
                res.append(path[:])
                return
            for end in range(start,len(s)):
                if ispalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end+1,path)
                    path.pop()
        backtrack(0,[])
        return res