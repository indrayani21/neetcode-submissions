class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        max_prod=nums[n-1]*nums[n-2]
        min_prod=nums[0]*nums[1]
        return max_prod-min_prod