class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # [9,1,1,1,2,3,1,10]
        # [1,1,1,2,3,1,9,10]
        # [1,1,1,2,1,3,9,10]
        # [1,1,1,1,2,3,9,10]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums