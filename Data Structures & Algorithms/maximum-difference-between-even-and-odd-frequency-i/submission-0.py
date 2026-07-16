class Solution:
    def maxDifference(self, s: str) -> int:
        oddmax,evenmin=0,float("inf")
        i=0
        while i<len(s):
            a=s.count(s[i])
            if a%2==1:
                oddmax=max(oddmax,a)
            else:
                evenmin=min(evenmin,a)
            i+=1
        return oddmax-evenmin
