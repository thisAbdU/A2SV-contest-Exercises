
def path_finder(graph):
    pass

def construct_graph(n, arr):
    graph = [[] for _ in range(n)]

    for i,j in arr:
        graph[i].append(j)
        graph[j].append(i)
    
    return graph

arr = [[0, 1], [0, 2], [2, 3]]
print(construct_graph(4, arr))
