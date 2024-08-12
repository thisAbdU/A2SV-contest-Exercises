class MazeSolver:
    def __init__(self, grid, n, m):
        self.grid = grid
        self.n = n
        self.m = m
        self.ans = 0
        self.visited = [[False for _ in range(m)] for _ in range(n)]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def inbound(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.m

    def dfs(self, row, col):
        if not self.inbound(row, col) or self.visited[row][col] or self.grid[row][col] == '#':
            return

        self.visited[row][col] = True

        if self.grid[row][col].isdigit():
            self.ans += int(self.grid[row][col])

        trap_nearby = False
        for dr, dc in self.directions:
            newRow, newCol = row + dr, col + dc
            if self.inbound(newRow, newCol) and self.grid[newRow][newCol] == 'T':
                trap_nearby = True
                break

        if not trap_nearby:
            for dr, dc in self.directions:
                self.dfs(row + dr, col + dc)

def solve_maze():
    while True:
        try:
            n, m = list(map(int, input().split()))
            grid = []

            for i in range(n):
                grid.append(list(input()))

            solver = MazeSolver(grid, n, m)

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == "S":
                        solver.dfs(i, j)

            print(solver.ans)

        except EOFError:
            break

solve_maze()
