
from collections import defaultdict


n_m = list(map(int, input().split()))
arr = []
for i in range(n_m[1]):
    col = list(map(int, input().split()))
    arr.append(col)


res = defaultdict(list)
for r in range(len(arr)):
    res[arr[r][0]].append(arr[r][1])
    res[arr[r][1]].append(arr[r][0])
lens = []
for i in range(1, n_m[1] + 1):
    lens.append(len(res[i]))

lens = list(set(lens))
if len(lens) == 1:
    print("ring topology")
elif len(lens) == 2 and min(lens) == 1 and max(lens) == 2:
    print("bus topology")
elif len(lens) == 2 and max(lens) == n_m[1]:
    print("star topology")
else:
    print("unknown topology")

# elif len(set(lens)) == 2:
#     if max(lens) == n_m[1]:
#         print("star topology")
#     if max(lens) - min(lens) == 1:
#         print("bus topology")
# else:
#     print("unknown topology")
