class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        intervals.sort()
        i, j = intervals[0]
        for k in range(1, len(intervals)):
            if j >= intervals[k][0]:
                j = max(j, intervals[k][1])
            else:
                l.append([i, j])
                i, j = intervals[k]
        l.append([i, j])
        return l
