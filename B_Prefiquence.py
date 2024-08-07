from typing import Counter


def prefiquence(a, b):
    count_b = Counter(b)
    k = 0
    for i in range(len(a)):
        if count_b[a[i]] > 0:
            count_b[a[i]] -= 1
            k += 1
        elif a[i] in count_b and count_b[a[i]] == 0:
            return k
        elif a[i] not in count_b:
            return k
    return k

test = int(input())
for t in range(test):
    n_a = list(map(int, input().split()))
    a = list(map(int, input()))
    b = list(map(int, input()))
    print(prefiquence(a, b))