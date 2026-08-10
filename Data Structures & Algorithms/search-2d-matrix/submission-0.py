class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        col_len = len(matrix[0])
        end = (len(matrix) * col_len) - 1        
        while start <= end:
            mid = start + (end - start) // 2
            row = mid // col_len
            col = mid % col_len
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False