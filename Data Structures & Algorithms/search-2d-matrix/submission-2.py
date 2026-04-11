class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_matrix = [item for row in matrix for item in row]
        left, right = 0, len(flattened_matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if flattened_matrix[mid] == target:
                return True
            elif flattened_matrix[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False