def gelada_baboon(n, arr):
    par = [i for i in range(n + 1)]
    rank = [1]*(len(arr) + 1)

    def find(x):
        p = par[x]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p
    
    def union(x1, x2):
        p1, p2 = find(x1), find(x2)
        
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]

        elif rank[p1] < rank[p2]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            if p1 < p2:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
    
    for i, n in enumerate(arr):
        union(n, i + 1)
    
    real_parent = set()
    for i in range(1, len(par)):
        real_parent.add(find(i))
    return len(set(real_parent))

n = int(input())
arr = list(map(int, input().split()))
print(gelada_baboon(n, arr))