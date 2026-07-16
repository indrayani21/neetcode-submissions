class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        max_total = nums[0]
        for right in range(1,len(nums)):
            if nums[right]>nums[right-1]:
                total+=nums[right]
            else:
                total=nums[right]
            max_total=max(max_total,total)
        return max_total