class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        longest=""
        for i in range(0,len(s)):
            oddlength=palindrome(i,i)
            evenlength=palindrome(i,i+1)
            longest=max(longest,oddlength,evenlength,key=len)
        return longest