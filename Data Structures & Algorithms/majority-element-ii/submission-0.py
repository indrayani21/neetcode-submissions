class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c=Counter(nums)
        a=[]
        for i,j in c.items():
            if j>n/3:
                a.append(i)
        return a