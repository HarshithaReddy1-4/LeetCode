class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        cols = len(matrix[0])
        h = (len(matrix) * cols) - 1
        
        while l <= h:
            mid = (l + h) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False