class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        hashmap={}
        left=0
        for right in range(0,len(s)):
            if s[right] in hashmap and hashmap[s[right]]>=left:
                left=hashmap[s[right]]+1
            hashmap[s[right]]=right
            longest=max(longest,right-left+1)
        return longest