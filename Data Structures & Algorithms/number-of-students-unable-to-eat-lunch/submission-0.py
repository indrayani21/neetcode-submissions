class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=[0,0]
        for s in students:
            count[s]+=1
        for sand in sandwiches:
            if count[sand]>0:
                count[sand]-=1
            else:
                break
        return count[0]+count[1]