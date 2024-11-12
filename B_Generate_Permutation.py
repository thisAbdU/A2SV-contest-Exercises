
for _ in range(int(input())):
    n = int(input()) 
    if n%2 == 0:
        print(-1)
    else:
        ans = [-1 for i in range(n)]
        for i in range(len(ans)//2, len(ans)):
            ans[i] = i - (len(ans)//2) + 1

        for i in range(len(ans)//2):
            ans[i] = len(ans) - i
        print(*ans)