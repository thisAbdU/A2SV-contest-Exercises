def vlad_and_shapes(grid):
    n = len(grid)
    triangle = False
    for i in range(n):
        if '1' in grid[i] and grid[i].count('1') == 1:
            triangle = True
            break

    if triangle:
        return "TRIANGLE"
    else:
        return "SQUARE"


t = int(input())

for _ in range(t):
    n = int(input())
    grid = [input() for _ in range(n)]
    print(vlad_and_shapes(grid))
