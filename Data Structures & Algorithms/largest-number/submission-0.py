from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
         # convert to string
        nums = list(map(str, nums))
        
        # custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)
        
        # edge case: all zeros
        return "0" if result[0] == '0' else result