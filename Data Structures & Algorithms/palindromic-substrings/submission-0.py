class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(i,j):
            count=0
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1
            return count
        total=0
        for i in range(0,len(s)):
            total+=palindrome(i,i)
            total+=palindrome(i,i+1)
        return total