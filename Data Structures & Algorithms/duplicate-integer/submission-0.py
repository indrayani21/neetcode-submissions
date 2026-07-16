from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for i,j in c.items():
            if j>1:
                return True
        return False