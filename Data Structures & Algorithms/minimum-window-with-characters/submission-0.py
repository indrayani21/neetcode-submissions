class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        char_map=defaultdict(int)
        for ch in t:
            char_map[ch]+=1
        target_chars_remaining=len(t)
        min_window=(0,float('inf')) # range of your current smallest miniumn window
        start_index=0 # left shrink index
        for end_index,ch in enumerate(s):
            if char_map[ch]>0:
                target_chars_remaining-=1
            char_map[ch]-=1
            if target_chars_remaining==0:
                while True:
                    char_at_start=s[start_index]
                    if char_map[char_at_start]==0: # you can't remove that character our window will become invalid
                        break
                    char_map[char_at_start]+=1
                    start_index+=1
                if end_index-start_index<min_window[1]-min_window[0]:
                    min_window=(start_index,end_index)
                char_map[s[start_index]]+=1
                target_chars_remaining+=1
                start_index+=1
        return "" if min_window[1]>len(s) else s[min_window[0]:min_window[1]+1]
