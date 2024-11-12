from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    query = []
    for _ in range(n):
        x_y = list(map(int, input().split()))
        query.append(x_y)
    
    query.sort(key=lambda x:x[-1])

    if query[0][-1] == query[-1][-1]:
        print(0)
        continue
    
    def count_right_triangles(points):
        x_count = defaultdict(int)
        y_count = defaultdict(int)
        
        for x, y in points:
            x_count[x] += 1
            y_count[y] += 1
        
        total_triangles = 0
        
        for x, y in points:
            v = x_count[x]
            h = y_count[y]
            total_triangles += (v - 1) * (h - 1)
        
        return total_triangles + 1


    print(count_right_triangles(query))