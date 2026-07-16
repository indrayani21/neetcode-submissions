from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        most_common=c.most_common(k)
        r=[i[0] for i in most_common]
        return r