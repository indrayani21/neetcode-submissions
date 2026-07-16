class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rot(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        i,n=0,len(nums)
        k = k % n
        rot(nums,i,n-1)
        rot(nums,i,k-1)
        rot(nums,k,n-1)
        return nums
        