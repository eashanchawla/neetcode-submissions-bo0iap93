import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult, non_zero_mult, num_zeros = 1, 1, 0
        zero_indices = []
        for i, num in enumerate(nums):
            if num == 0:
                num_zeros += 1
                zero_indices.append(i)
            else:
                non_zero_mult *= num
            mult *= num
        result = []
        if num_zeros > 1:
            return [0] * len(nums)
        elif num_zeros == 1:
            result = [0] * len(nums)
            result[zero_indices[0]] = non_zero_mult
        else:
            result = [mult // num for num in nums]

        return result
            
        