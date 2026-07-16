class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights.sort()
        max_area=0
        low,high=0,len(heights)-1
        while low<=high:
            width=high-low
            h=min(heights[low],heights[high])
            max_area=max(max_area,h*width)
            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1
        return max_area