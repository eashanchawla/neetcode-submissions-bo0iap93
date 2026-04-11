class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []
        i = 0
        while (i < len(intervals)) and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1
        
        # while there is any overlap
        while (i < len(intervals)) and (newInterval[0] <= intervals[i][1] and intervals[i][0] <= newInterval[1]):
            newStart = min(newInterval[0], intervals[i][0])
            newEnd = max(newInterval[1], intervals[i][1])
            i += 1
            newInterval = [newStart, newEnd]

        merged_intervals.append(newInterval)
        
        while i < len(intervals):
            merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals