class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=Counter(nums)
        for key,val in freq.items():
            if val>1:
                return key
                