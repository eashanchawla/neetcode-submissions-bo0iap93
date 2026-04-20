from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        numCo = [(-v, k) for k, v in c.items()]
        heapq.heapify(numCo)
        return [heapq.heappop(numCo)[1] for _ in range(k)]