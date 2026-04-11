class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = set()

        for i, fixed_number in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                combo = nums[l] + nums[r] + fixed_number
                if combo == 0:
                    solution.add((fixed_number, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif combo < 0:
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in solution]