"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # 🔹 sort by start time
        intervals.sort(key=lambda x: x.start)
        
        heap = []
        
        # push first meeting end
        heapq.heappush(heap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            
            # reuse room if possible
            if start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)