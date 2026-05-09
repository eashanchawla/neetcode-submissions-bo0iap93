class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        maxseq = 0

        for number in d:
            if number - 1 in d:
                continue
            else:
                streak = 1
                start = number + 1
                while start in d:
                    streak += 1
                    start += 1
                maxseq = max(maxseq, streak)
        return maxseq