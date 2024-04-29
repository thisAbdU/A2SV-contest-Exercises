from bisect import bisect_left


def yikes(labels, jucy):
    for i in range(1, len(labels)):
        labels[i] += labels[i - 1]
    for i in range(len(jucy)):
        position = bisect_left(labels, jucy[i], 0, len(labels))
        print(position + 1)
    return

n = int(input())
labels = list(map(int, input().split()))
j = int(input())
juc = list(map(int, input().split()))
yikes(labels, juc)
