class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=Counter(ransomNote)
        c2=Counter(magazine)
        for ch in c1:
            if c1[ch]>c2.get(ch,0):
                return False
        return True