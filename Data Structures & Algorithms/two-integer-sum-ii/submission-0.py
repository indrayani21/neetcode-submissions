class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            sum=0
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target and i<j:
                    return[i+1,j+1]