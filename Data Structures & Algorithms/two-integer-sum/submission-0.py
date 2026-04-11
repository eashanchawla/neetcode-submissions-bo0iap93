class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i, num in enumerate(nums):
            if (target - num) in hmap.keys():
                return [hmap[(target-num)], i]
            else:
                hmap[num] = i