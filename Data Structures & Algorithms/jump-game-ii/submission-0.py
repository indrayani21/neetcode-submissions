class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        farthest=0
        end=0
        jumps=0
        for i in range(0,len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==end:
                jumps+=1
                end=farthest
        return jumps
