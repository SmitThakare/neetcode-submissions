"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        
        # Min heap to track end times of ongoing meetings
        heap = []
        
        for interval in intervals:
            # If earliest meeting has ended, reuse its room
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            
            # Add current meeting's end time
            heapq.heappush(heap, interval.end)
        
        # Heap size = number of rooms needed
        return len(heap)