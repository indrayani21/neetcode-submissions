class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        low,high=0,m
        while low<=high:
            partionX=(low+high)//2
            partionY=(m+n+1)//2-partionX

            maxLeftX=float("-inf") if partionX==0 else nums1[partionX-1]
            minRightX=float("inf") if partionX==m else nums1[partionX]

            maxLeftY=float("-inf") if partionY==0 else nums2[partionY-1]
            minRightY=float("inf") if partionY==n else nums2[partionY]

            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (m+n)%2==0:
                    return (max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2
                else:
                    return max(maxLeftX,maxLeftY)
            elif maxLeftX>minRightY:
                high=partionX-1
            else:
                low=partionX+1