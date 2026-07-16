class Solution:
    def maxScore(self, s: str) -> int:
        max_score=0
        for i in range(1,len(s)):
            c1=s[:i]
            c2=s[i:]
            score=c1.count("0")+c2.count("1")
            max_score=max(max_score,score)
        return max_score

