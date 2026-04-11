class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        # if it's not even in the bounds of the matrix
        if target < matrix[top][0] or target > matrix[bottom][-1]:
            return False

        target_row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target >= matrix[mid][0]:
                if target <= matrix[mid][-1]:
                    # search on this row
                    left, right = 0, columns - 1
                    while left <= right:
                        mid_r = (left + right) // 2
                        if target == matrix[mid][mid_r]:
                            return True
                        elif target > matrix[mid][mid_r]:
                            left = mid_r + 1
                        else:
                            right = mid_r - 1 
                    return False
                else:
                    top = mid + 1
            else:
                bottom = mid - 1
        return False