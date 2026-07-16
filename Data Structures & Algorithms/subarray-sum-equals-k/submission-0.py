class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=0
        count=0
        prefix={0:1}
        for i in nums:
            total+=i
            if total-k in prefix:
                count+=prefix[total-k]
            prefix[total]=prefix.get(total,0)+1
        return count