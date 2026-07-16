class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern) != len(s):   # ✅ important
            return False
        s_map={}
        t_map={}
        for i in range(0,len(pattern)):
            if pattern[i] in s_map:
                if s_map[pattern[i]]!=s[i]:
                    return False
            else:
                s_map[pattern[i]]=s[i]
            if s[i] in t_map:
                if t_map[s[i]]!=pattern[i]:
                    return False
            else:
                t_map[s[i]]=pattern[i]
        return True