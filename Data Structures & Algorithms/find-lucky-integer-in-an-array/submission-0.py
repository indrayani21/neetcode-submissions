class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        ans=-1
        for k,v in freq.items():
            if k==v:
                ans=max(ans, k)
        return ans