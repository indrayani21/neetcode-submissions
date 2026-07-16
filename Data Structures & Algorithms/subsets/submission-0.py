class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(ans,i):
            if i==len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[i])
            backtrack(ans,i+1)
            ans.pop()
            backtrack(ans,i+1)
        backtrack([],0)
        return res