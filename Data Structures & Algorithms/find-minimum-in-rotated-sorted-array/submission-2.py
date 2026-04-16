class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                # there is an inflection point i.e. minimum to the right
                left = middle + 1
            else:
                # min is at middle or to the left of it 
                right = middle
        
        return nums[left]