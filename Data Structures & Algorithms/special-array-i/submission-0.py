class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            if nums[i] % 2 == nums[j] % 2:
                return False
            i+=1
            j+=1
        return True