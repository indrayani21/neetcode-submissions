class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        for i in range(0,len(arr)-k+1):
            comp=(arr[i:i+k])
            avg=sum(comp)//len(comp)
            if avg>=threshold:
                count+=1
        return count
