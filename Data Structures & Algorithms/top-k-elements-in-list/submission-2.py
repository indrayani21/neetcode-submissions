class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        a=sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        return a[:k]
