"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_end = float("-inf")
        intervals.sort(key = lambda i:i.start)
        for i in intervals:
            if i.start >= prev_end:
                prev_end = i.end
            else:
                prev_end = min(prev_end, i.end)
                return False
        return True

