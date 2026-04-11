class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = []
        for i in range(2 * len(nums)):
            newNums.append(nums[i % len(nums)])
        return newNums