class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ispossible(piles,mid,h):
            hours=0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            return hours<=h
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if ispossible(piles,mid,h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans