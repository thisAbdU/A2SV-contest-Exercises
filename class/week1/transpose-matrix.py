class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        index = defaultdict(int)
        row, col = len(matrix[0]), len(matrix)
        output = [[0 for i in range(col)] for j in range(row)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                index[(j, i)] = matrix[i][j]
        for i in range(len(output)):
            for j in range(len(output[0])):
                output[i][j] = index[(i, j)]
        return output