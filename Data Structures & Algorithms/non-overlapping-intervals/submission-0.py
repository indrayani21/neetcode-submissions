class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=[intervals[0]]
        count=0
        for i in range(1,len(intervals)):
            if res[-1][1]>intervals[i][0]: #previous_end > current_start -> overlap so we need to remove one but which one?
                count+=1
                if intervals[i][1] < res[-1][1]: #Remove the one with larger end time. Why? Because smaller end gives more space for future intervals. a it is our goal to return min removal
                    res[-1] = intervals[i]
            else:
                res.append(intervals[i])
        return count