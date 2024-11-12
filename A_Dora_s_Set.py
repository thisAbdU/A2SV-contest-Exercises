import math

def can_form_triplet(a, b, c):
    return math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1

def max_operations(l, r):
    numbers = list(range(l, r+1))
    operations = 0
    
    while len(numbers) >= 3:
        found = False
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    if can_form_triplet(numbers[i], numbers[j], numbers[k]):
                        # If a valid triplet is found, remove these elements
                        numbers.pop(k)
                        numbers.pop(j)
                        numbers.pop(i)
                        operations += 1
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            break
    
    return operations

# Input Reading and Processing
t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    results.append(max_operations(l, r))

# Output Results
for result in results:
    print(result)
