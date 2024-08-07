import sys


def num():
    return int(sys.stdin.readline().strip())
def st():
    return sys.stdin.readline().strip()

len_ = num()
word = st()

indexs = []
sum_ = 0

for i in range(len_):
    sum_ += i
    if sum_ >= len_:
        break
    indexs.append(sum_)

res = []
for n in indexs:
    res.append(word[n])
print("".join(res))


