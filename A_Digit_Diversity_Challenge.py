l, r = map(int, input().split())

def has_unique_digits(num):
    num_str = str(num)
    return len(set(num_str)) == len(num_str)

found = False

for x in range(l, r + 1):
    if has_unique_digits(x):
        print(x)
        found = True
        break

if not found:
    print(-1)
