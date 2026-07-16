class Solution:
    def isValid(self, s: str) -> bool:
        parenthese={')':'(',"}":"{","]":"["}
        stack=[]
        for i in range(0,len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack or stack[-1]!=parenthese[s[i]]:
                    return False
                stack.pop()
        return len(stack)==0
                