class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key = lambda i: i[0])
            output = [intervals[0]]

            for current_start, current_end in intervals[1:]:
                prev_interval = output[-1]

                if current_start <= prev_interval[1]:
                    prev_interval[1] = max(prev_interval[1], current_end)
                else:
                    output.append([current_start, current_end])
            return output