class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix_sum={0:1}
        total=0
        for right in range(0,len(nums)):
            total+=nums[right]
            if total-goal in prefix_sum:
                count+=prefix_sum[total-goal]
            prefix_sum[total]=prefix_sum.get(total,0)+1
        return count

