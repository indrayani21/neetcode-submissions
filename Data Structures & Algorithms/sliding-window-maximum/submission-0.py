class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a=[]
        for i in range(len(nums)-k+1):
            window=nums[i:i+k]
            a.append(max(window))
        return a
