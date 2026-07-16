class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c=Counter(nums)
        for i,j in c.items():
            if j>n/2:
                return i
                