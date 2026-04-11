class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        duck = {i: 1 for i in range(len(nums))}
        for i in range(len(nums)):
            number = nums[i]
            for key in duck:
                if key != i:
                    duck[key] *= number
        return list(duck.values())