class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target <= matrix[middle][-1]:
                # secondary binary search
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    c = (left + right) // 2
                    if matrix[middle][c] == target:
                        return True
                    elif target > matrix[middle][c]:
                        left = c + 1
                    else:
                        right = c - 1
                return False
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                top = middle + 1
        return False