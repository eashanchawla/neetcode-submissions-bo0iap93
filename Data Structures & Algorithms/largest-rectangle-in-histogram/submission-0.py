class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i = 0
        stack = []
        max_area = 0

        while i < len(heights):
            while stack and heights[i] < heights[stack[-1]]:
                    # can go on no longer on the right
                    pop_index = stack.pop()
                    height = heights[pop_index]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i
                    max_area = max(max_area, height * width)

            stack.append(i)
            i += 1
        
        while stack: 
            pop_index = stack.pop()
            height = heights[pop_index]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)
            
            max_area = max(max_area, width * height)

        return max_area