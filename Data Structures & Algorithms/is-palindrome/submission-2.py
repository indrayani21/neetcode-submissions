class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        s=s.lower()
        for i in range(0,len(s)):
            if s[i].isalnum():
                res+=s[i]
        return res==res[::-1]