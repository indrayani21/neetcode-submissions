class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # count of each number should be divisible by 2
        freq=Counter(nums)
        for count in freq.values():
            if count%2!=0:
                return False
        return True