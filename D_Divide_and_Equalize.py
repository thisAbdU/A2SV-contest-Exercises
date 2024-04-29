def add_divs(x, divs):
    i = 2
    while i * i <= x:
        while x % i == 0:
            divs[i] = divs.get(i, 0) + 1
            x //= i
        i += 1
    if x > 1:
        divs[x] = divs.get(x, 0) + 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    divs = {}
    for num in a:
        add_divs(num, divs)
    for val in divs.values():
        if val % n != 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print("YES" if solve() else "NO")
