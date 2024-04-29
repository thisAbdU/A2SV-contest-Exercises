n = int(input())
scores = list(map(int, input().split()))

# Sort the array
scores.sort()

# Count the number of adjacent pairs where ai+1 > ai
happy_count = sum(scores[i] < scores[i + 1] for i in range(n - 1))

print(happy_count)
