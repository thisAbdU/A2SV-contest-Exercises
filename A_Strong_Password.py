def solve():
    s = input().strip()
    n = len(s)
    idx = -1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            idx = i
            break
    if idx == -1:
        if s[-1] == 'a':
            print(s + 'b')
        else:
            print(s + 'a')
    else:
        t = 'a'
        if s[idx] == 'a':
            t = 'b'
        print(s[:idx + 1] + t + s[idx + 1:])

def main():
    t = int(input().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()