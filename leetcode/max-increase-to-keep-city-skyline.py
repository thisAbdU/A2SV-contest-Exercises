class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x = list(zip(*grid))
        max1 = []
        max2 =[]
        output = 0
        for i in range(len(grid)):
            max1.append(max(grid[i]))
            max2.append(max(x[i]))
        for i in range(len(grid)):
            for j in range(len(grid)):
                output += (min(max1[i],max2[j])-grid[i][j])
        return output
