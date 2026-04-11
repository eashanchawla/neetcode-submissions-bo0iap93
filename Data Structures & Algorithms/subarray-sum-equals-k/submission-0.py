from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = defaultdict(int)
        result, current_sum = 0, 0
        subarray[0] = 1

        for number in nums:
            current_sum += number
            search = current_sum - k
            if search in subarray:
                result+= subarray[search]
            subarray[current_sum] += 1
        return result