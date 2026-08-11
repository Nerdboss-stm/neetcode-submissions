class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowOuter = 0
        highOuter = len(matrix) - 1
        while lowOuter <= highOuter:
            row = (lowOuter+highOuter)//2
            if target > matrix[row][-1]:
                lowOuter = row + 1
            elif target < matrix[row][0]:
                highOuter = row -1
            else:
                break
        
        if not lowOuter <= highOuter:
            return False
        lowInner = 0
        highInner = len(matrix[0]) - 1
        while lowInner <= highInner:
            mid = (lowInner + highInner) // 2
            if matrix[row][mid] > target:
                highInner = mid - 1
            elif matrix[row][mid] < target:
                lowInner = mid + 1
            else:
                return True
        return False