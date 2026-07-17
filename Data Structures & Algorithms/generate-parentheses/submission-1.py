class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(curr,opens,close):
            if len(curr)==2*n: # base case
                res.append(curr)
                return
            if opens<n:
                backtrack(curr+"(",opens+1,close)
            if close<opens:
                backtrack(curr+")",opens,close+1)
        backtrack("",0,0)
        return res