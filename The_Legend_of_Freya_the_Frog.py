import math

for _ in range(int(input())):
    x, y, k = map(int, input().split())

    moves_x = math.ceil(x / k)
    moves_y = math.ceil(y / k)

    if moves_x > moves_y:
        print(2 * max(moves_x, moves_y) - 1)
    else:
        print(2 * max(moves_x, moves_y))
