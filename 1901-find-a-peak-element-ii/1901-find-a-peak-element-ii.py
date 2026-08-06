class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        while low <= high:
            mid = (low + high) // 2

            matRow = 0
            for i in range(rows):
                if mat[i][mid] > mat[matRow][mid]:
                    matRow = i

            left = mat[matRow][mid - 1] if mid >0 else -1
            right = mat[matRow][mid + 1] if mid < cols - 1 else -1

            if mat[matRow][mid] >= left and mat[matRow][mid] >= right:
                return [matRow, mid]

            elif left > mat[matRow][mid]:
                high = mid - 1

            else:
                low = mid + 1
