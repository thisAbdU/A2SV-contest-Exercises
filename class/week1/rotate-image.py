class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, 0
        for row in range(i, len(matrix)):
            for col in range(j, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            i += 1
            j += 1

        for i in range(len(matrix)):
            leftPt, rightPt = 0, len(matrix) - 1
            while leftPt < rightPt:
                matrix[i][leftPt], matrix[i][rightPt] = matrix[i][rightPt], matrix[i][leftPt]
                leftPt += 1
                rightPt -= 1
        