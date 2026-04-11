class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_unique_index = 0
        unique_nums = 1
        for i in range(1, len(nums)):
            if nums[last_unique_index] != nums[i]:
                # found a new unique value, add it to next index
                nums[last_unique_index + 1] = nums[i]
                last_unique_index += 1
                unique_nums += 1
        return last_unique_index + 1