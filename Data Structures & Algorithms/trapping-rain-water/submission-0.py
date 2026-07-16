class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0]
        right_max=[]
        trap_water=[]
        res=0
        for i in range(0,len(height)):
            left_max.append(max(height[0:i+1]))
        for i in range(0,len(height)):
            right_max.append(max(height[i:len(height)]))
        for i in range(0,len(height)):
            trap_water.append(min(left_max[i],right_max[i])-height[i])
            if min(left_max[i],right_max[i])-height[i]>0:
                res=res+min(left_max[i],right_max[i])-height[i]
        return res