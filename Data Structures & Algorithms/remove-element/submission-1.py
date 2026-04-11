class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        numVals = 0
        while l <= r:
            if nums[r] == val:
                r -= 1
                numVals += 1
            elif nums[l] == val:
                # swap l and r
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
                r -= 1
                numVals += 1
            else:
                l += 1
        return len(nums) - numVals
