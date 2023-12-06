from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        output = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                output.append(matrix[j][right])
            right -= 1

            if top <= bottom:  # Check to avoid duplicate rows
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:  # Check to avoid duplicate columns
                for j in range(bottom, top - 1, -1):
                    output.append(matrix[j][left])
                left += 1

        return output
