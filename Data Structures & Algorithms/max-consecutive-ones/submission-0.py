class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        count=0
        max_count_ones=0
        while i<len(nums):
            if nums[i]==1:
                count+=1
            else:
                count=0
            max_count_ones=max(max_count_ones,count)
            i+=1
        return max_count_ones