class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        def backtrack(target,i):
            if target==0:
                res.append(comb[:])
                return
            if target<0 or i==len(nums):
                return
            comb.append(nums[i])
            backtrack(target-nums[i],i)
            comb.pop()
            backtrack(target,i+1)
        backtrack(target,0)
        return res