def bfs(graph):
    queue = deque([])









courses = [[1, 2], [2, 3], [4, 5], [5], [], []]

graph = [[] for _ in range(len(courses))]
for i, course in enumerate(courses):
    for j in course:
        graph[j].append(i)
print(graph)