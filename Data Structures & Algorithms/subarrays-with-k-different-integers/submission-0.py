class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    
    def atMost(self, nums, k):
        left = 0
        count = defaultdict(int)
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1
        
        return result