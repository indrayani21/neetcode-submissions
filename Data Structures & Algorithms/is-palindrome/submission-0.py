class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum(): 
                w += s[i].lower()  # also fix case
        t = ""
        for i in s:
            if i.isalnum():
                t += i.lower()
        if t==w:
            return True
        else:
            return False