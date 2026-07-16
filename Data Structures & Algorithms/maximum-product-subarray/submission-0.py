class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        pref=1
        suff=1
        max_prod=float("-inf")
        for i in range(0,len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref=nums[i]*pref
            suff=nums[n-i-1]*suff
            max_prod=max(max_prod,max(pref,suff))
        return max_prod