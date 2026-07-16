class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(1,len(arr)):
            comp=max(arr[i:])
            arr[i-1]=comp
        arr[-1]=-1
        return arr