"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        intervals.sort(key = lambda x:x.start)
        for i in intervals:
            events.append((i.start, +1))
            events.append((i.end, -1))
        events.sort()
        best = curr = 0
        for _, delta in events:
            curr += delta
            best = max(best, curr)
        return best
        