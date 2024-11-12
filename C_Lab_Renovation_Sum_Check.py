n = int(input())
arr = []

for _ in range(n):
    rows = list(map(int, input().split()))
    arr.append(rows)

def solve():
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 1:
                found = False
                for s in range(n):
                    for t in range(n):
                        if arr[i][j] == arr[i][s] + arr[t][j]:
                            found = True
                            break
                    if found:
                        break
                if not found:
                    return "No"
    return "Yes"

print(solve())