class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=[]
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                val=(j-i)*min(heights[i],heights[j])
                area.append(val)
        return max(area)