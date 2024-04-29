from bisect import bisect_right

def spaceship_attack(space, defen_gold):
    defen_gold.sort()
    
    bases = []
    for b in defen_gold:
        y = b[0]
        bases.append(y)
    
    g = []
    for base in defen_gold:
        x = base[1]
        g.append(x)
    
    for i in range(1, len(g)):
        g[i] += g[i-1]

    golds = []
    for i in range(len(space)):
        pos = bisect_right(bases, space[i])
        if pos == 0:
            golds.append(0)
        else:
            golds.append(g[pos - 1])
        

    print(*golds)
    return

n_k = list(map(int, input().split()))


space = list(map(int, input().split()))
defe_gold = []
for i in range(n_k[1]):
    def_gold = list(map(int, input().split()))
    defe_gold.append(def_gold)
spaceship_attack(space, defe_gold)
