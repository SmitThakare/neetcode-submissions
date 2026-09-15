"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        n=len(intervals)
        m=0
        for i in range(1,n):
            if intervals[m].end>intervals[i].start:
                return False 
            else:
                m+=1
        return True 