class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_len=0
        for i in nums_set:
            if i-1 not in nums_set:
                curr=i
                length=1
                while curr+1 in nums_set:
                    curr+=1
                    length+=1
                max_len=max(max_len,length)
        return max_len