class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(ans,i):
            if i==len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[i])
            backtrack(ans,i+1)
            ans.pop()
            idx=i+1
            while idx<len(nums) and nums[idx]==nums[idx-1]:
                idx+=1
            backtrack(ans,idx)
        backtrack([],0)
        return res