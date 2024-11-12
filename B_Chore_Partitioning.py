n, a, b = list(map(int, input().split()))
h = list(map(int, input().split()))

h.sort()

print(h[-a] - h[-a - 1])