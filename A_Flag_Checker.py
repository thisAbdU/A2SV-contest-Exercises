def flag_checker(arr):
    rs = []
    for row in range(len(arr)):
        if len(set(arr[row])) != 1:
            return "NO"
        else:
            rs.append(arr[row][0])
    for i in range(1, len(rs)):
        if rs[i] == rs[i-1]:
            return "NO"
    return "YES"


n_m = list(map(int, input().split()))
arr = []
for i in range(n_m[0]):
    col = input()
    arr.append(list(map(int, col)))
print(flag_checker(arr))