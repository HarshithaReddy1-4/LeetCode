class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        start, end = intervals[0]
        for i, j in intervals[1:]:
            if i >= end:
                end = j
            else:
                count += 1
        return count
        