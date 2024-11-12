class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

n, m = list(map(int, input().split()))
inp = []
for _ in range(m):
    t, a, b = list(input().split())
    inp.append([t, int(a) - 1, int(b) - 1]) 

uf = UnionFind(n)

for i in range(len(inp)):
    uf.union(inp[i][1], inp[i][2])

res = set()
for i in range(n):
    res.add(uf.find(i))
print(bin(2 **len(res))[2:])


