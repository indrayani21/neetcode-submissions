class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a,b=set(nums1),set(nums2)
        diff1=a.difference(b)
        diff2=b.difference(a)
        answer=[0]*2
        answer[0]=list(diff1)
        answer[1]=list(diff2)
        return answer