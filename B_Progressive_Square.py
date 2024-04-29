def progressive_square(n_c_d, arr):
    n, c, d = n_c_d
    min_r = min(arr)
    pre = 0
    for i in range(n):
        pre += min_r
        min_r += d
        if min_r  not in arr:
            return "NO"
    min_r = min_r - pre + min(arr)
    min_r += c


# tes = int(input())
# for t in range(tes):
#     n_c_d = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     print(progressive_square(n_c_d, arr))
n_c_d = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(progressive_square(n_c_d, arr))