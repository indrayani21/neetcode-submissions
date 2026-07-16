class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        for part in path:
            if part=="" or part==".":
                continue
            elif part=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/"+"/".join(stack)
                

