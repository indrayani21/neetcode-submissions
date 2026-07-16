import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ops=0
        for f in freq.values():
            if f==1:
                return -1
            ops+=math.ceil(f/3)
        return ops