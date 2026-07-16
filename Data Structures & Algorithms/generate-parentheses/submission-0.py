class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis when open<n
        # only add closed parenthesis when closed<open
        stack=[]
        res=[]
        def backtrack(openN,closedN):
            if openN==closedN==n: #base case denotes found valid parenthesis
                res.append(''.join(stack))
                return 
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
