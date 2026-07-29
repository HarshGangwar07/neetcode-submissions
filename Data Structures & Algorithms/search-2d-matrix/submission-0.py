class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r = len(matrix)
        c = len(matrix[0])
        beg = 0
        end = r * c
        while beg < end:
            mid = beg + (end - beg) // 2
            idx = matrix[mid // c][mid % c]
            if idx == target:
                return True
            if idx < target:
                beg = mid + 1
            else:
                end = mid
        return False