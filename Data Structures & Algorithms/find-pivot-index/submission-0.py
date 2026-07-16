class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cum_sum=[0]*len(nums)
        cum_sum[0]=nums[0]
        for i in range(1,len(nums)):
            cum_sum[i]=cum_sum[i-1]+nums[i]
        total=sum(nums)
        for i in range(0,len(nums)):
            if i==0:
                left_sum=0
            elif i>0:
                left_sum=cum_sum[i-1]
            right_sum = total - left_sum - nums[i]
            if left_sum==right_sum:
                return i
        return -1
        