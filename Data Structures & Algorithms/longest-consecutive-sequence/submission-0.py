from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = Counter(nums)
        maxseq = 0
        while len(nums) > 0:
            min_num = min(nums)
            bf = False
            lsq = []
            i = min_num
            while True:
                if i in nums:
                    nums.remove(i)
                    lsq.append(i)
                    i += 1
                else:
                    break
            maxseq = max(maxseq, len(lsq))
        return maxseq