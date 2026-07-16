class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ispossible(piles,h,mid):
            total_hours=0
            for p in piles:
                total_hours += (p + mid - 1) // mid
            return total_hours<=h
        start=1
        end=max(piles)
        ans=-1
        while start<=end:
            mid=start+(end-start)//2
            if ispossible(piles,h,mid):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
