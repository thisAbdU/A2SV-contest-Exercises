from sys import stdin, stdout

INF = int(1e9)
vars = ["BG", "BR", "BY", "GR", "GY", "RY"]

def main():
    input = stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    while t > 0:
        t -= 1
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        a = []
        for i in range(n):
            s = data[index]
            a.append(vars.index(s))
            index += 1
        
        lf = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        
        for o in range(2):
            last = [-INF] * 6
            for i in range(n):
                if o == 1:
                    last[a[i]] = n - i - 1
                    rg[n - i - 1] = last[:]
                else:
                    last[a[i]] = i
                    lf[i] = last[:]
            a.reverse()

        while q > 0:
            q -= 1
            x = int(data[index]) - 1
            y = int(data[index + 1]) - 1
            index += 2
            
            ans = INF
            for j in range(6):
                if a[x] + j != 5 and j + a[y] != 5:
                    ans = min(ans, abs(x - lf[x][j]) + abs(lf[x][j] - y))
                    ans = min(ans, abs(x - rg[x][j]) + abs(rg[x][j] - y))
            
            if ans > INF // 2:
                ans = -1
            results.append(str(ans))
       
    stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
