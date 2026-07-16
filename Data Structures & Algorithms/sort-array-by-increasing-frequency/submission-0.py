class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        nums.sort(key=lambda n: (freq[n],-n))
        return nums