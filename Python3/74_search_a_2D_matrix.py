https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        middleRow = 0

        while top <= bottom:
            middleRow = (top + bottom) // 2
            if matrix[middleRow][-1] < target:
                top += 1
            elif matrix[middleRow][0] > target:
                bottom -= 1
            else:
                break

        left = 0
        right = COLS - 1

        while left <= right:
            middleCol = (left + right) // 2
            if matrix[middleRow][middleCol] < target:
                left += 1
            elif matrix[middleRow][middleCol] > target:
                right -= 1
            else:
                return True

        return False

