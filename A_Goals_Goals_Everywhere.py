for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max_goal = sum(arr)
    min_goal = 0

    for c in arr:
        min_goal = max(min_goal, c)

    print(max(min_goal, (max_goal+1)//2), max_goal)