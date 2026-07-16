class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=Counter(list(s))
        s2=Counter(list(t))
        if len(s)!=len(t):
            return False
        elif s1!=s2:
            return False
        else:
            for i in range(0,len(s)):
                if s[i] in t:
                    if i==len(s)-1:
                        return True
            return False