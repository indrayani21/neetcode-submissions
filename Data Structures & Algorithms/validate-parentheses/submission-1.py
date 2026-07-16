class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ["()", "[]", "{}"]
        s = list(s) #([{}])-> ["(","[","{","}","]",")"]
        i = 0
        while i < len(s) - 1:
            pair = s[i] + s[i+1]
            if pair in pairs:
                # Remove the matched pair and restart from the beginning
                s.pop(i)
                s.pop(i)  # i+1 shifted to i after pop
                i = 0
            else:
                i += 1
        return len(s) == 0