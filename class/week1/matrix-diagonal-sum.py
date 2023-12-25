class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            # Add elements from the primary diagonal
            diagonal_sum += mat[i][i]

            # Add elements from the secondary diagonal (excluding common elements)
            j = n - i - 1
            if i != j:
                diagonal_sum += mat[i][j]

        return diagonal_sum
