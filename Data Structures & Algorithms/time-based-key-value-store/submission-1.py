from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.kv_cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        current_list = self.kv_cache[key]
        left, right = 0, len(current_list) - 1
        min_val, min_ts = '', float('-inf')
        while left <= right:
            mid = (left + right) // 2

            if timestamp >= current_list[mid][1]:
                left = mid + 1
                if current_list[mid][1] > min_ts:
                    min_val, min_ts = current_list[mid]
            else:
                right = mid - 1
        if len(current_list) > 0 and min_val == '' and current_list[-1][1] <= timestamp:
            return current_list[-1][0]
        return min_val

