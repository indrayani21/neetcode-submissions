class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        p=[]
        count=0
        for i in range(0,len(position)):
            t=((target-position[i])/speed[i])
            time.append(t) #[3,3]
            (p.append((position[i],time[i])))
            p.sort()
        p=p[::-1]
        max_time = 0
        for pos, t in p:
            if t > max_time:
                count += 1
                max_time = t
        return count
         #[(1,3),(4,3)]