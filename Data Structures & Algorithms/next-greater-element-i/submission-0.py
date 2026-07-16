class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge_map = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)
        
        # remaining elements have no next greater
        for num in stack:
            nge_map[num] = -1
        
        return [nge_map[num] for num in nums1]  