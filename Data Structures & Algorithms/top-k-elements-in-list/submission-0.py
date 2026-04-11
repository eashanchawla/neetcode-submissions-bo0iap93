from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        x_heap = [(-v, k) for k, v in x.items()]
        heapq.heapify(x_heap)
        return [heapq.heappop(x_heap)[1] for _ in range(k)]