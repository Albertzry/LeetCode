class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        i = 0
        while i<len(intervals):
            j = i+1
            while j < len(intervals):
                if intervals[j][1] <= intervals[i][1]:
                    intervals.pop(j)
                    continue
                j+=1
            i+=1
        return len(intervals)