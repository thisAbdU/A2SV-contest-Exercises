def solve():
    n, p = list(map(int, input().split()))

    def giver():
        l = 1
        h = n
        ans = h
        while l<=h:
            mid = (l+h)//2

            su = ((p-mid+1)*(mid+p))//2
            if su <= n:
                ans = min(ans, mid)
                h = mid-1
            else:
                l = mid+1
        return ans
    
    diff = min(p, p - giver())

    upto = (diff*(diff + 1))//2

    max_ = n * (diff + 2)

    appear = (diff + 1) * giver()

    total = max_ - ()
for _ in range(int(input())):
    solve()