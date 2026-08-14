class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals, prev_end = 0, float("-inf")
        intervals.sort()
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1
                prev_end = min (prev_end, end)
        return removals
        