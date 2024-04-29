from collections import defaultdict


def maximum_saving(input_network: str) -> int:
    """
    This function calculates the maximum saving that can be achieved by removing
    redundant edges while ensuring the network remains connected.

    Args:
        input_network: A string representation of the network adjacency matrix.

    Returns:
        The maximum saving as an integer.
    """

    adjacency_matrix, edge_costs = parse_network(input_network)  

    mst_cost = prim_mst(adjacency_matrix)
    total_cost = calculate_total_cost(edge_costs) 

   
    max_possible_cost = total_cost - mst_cost

    max_saving = total_cost - max_possible_cost

    return calculate_unique_total_cost(adjacency_matrix) - max_saving

def prim_mst(graph):
    """
    This function implements Prim's algorithm to find the minimum spanning tree of the graph.

    Args:
        graph: A dictionary representing the adjacency matrix.

    Returns:
        The total cost of the minimum spanning tree as an integer.
    """

    parents = [-1] * len(graph)
    key = [float('inf')] * len(graph)
    mst_set = [False] * len(graph)

    key[0] = 0    
    count = 0

    while count < len(graph):
        u = min_key(key, mst_set)

        mst_set[u] = True

        for v, weight in graph[u].items():
            if mst_set[v] == False and weight < key[v]:
                parents[v] = u
                key[v] = weight

        count += 1

    total_mst_cost = 0
    for i in range(1, len(graph)):
        total_mst_cost += graph[i][parents[i]]

    return total_mst_cost

def min_key(key, mst_set):
    """
    This function finds the vertex with minimum key value, from
    the set of vertices not yet included in MST
    """
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if mst_set[v] == False and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index

def calculate_total_cost(edge_costs):
    """
    This function calculates the total cost of the network represented by the edge costs.

    Args:
        edge_costs: A dictionary representing the costs of each edge.

    Returns:
        The total cost as an integer.
    """
    return sum(edge_costs.values())

def parse_network(network_str):
    """
    This function parses the input network string into an adjacency matrix and keeps track of edge costs.

    Args:
        network_str: A string representation of the network adjacency matrix.

    Returns:
        A tuple containing the adjacency matrix and a dictionary of edge costs.
    """

    rows = network_str.splitlines()
    rows = [row.strip() for row in rows if row.strip()]
    num_nodes = len(rows[0])

    adjacency_matrix = defaultdict(dict)
    edge_costs = {}  # Dictionary to store total cost between nodes (handles duplicates)

    for i, row in enumerate(rows):
        values = row.split(',')
        for j, value in enumerate(values):
            if i != j and value.strip() and value.strip() != '-':
                cost = int(value.strip())
                if (i, j) not in edge_costs: 
                    edge_costs[(i, j)] = cost
                    adjacency_matrix[i][j] = cost
                else:
                    edge_costs[(i, j)] += cost  
                    adjacency_matrix[i][j] = edge_costs[(i, j)] 

    return adjacency_matrix, edge_costs

def calculate_unique_total_cost(adjacency_matrix):
    """
    This function calculates the total cost of the network represented by the adjacency matrix,
    considering only one route between any pair of nodes.

    Args:
        adjacency_matrix: A dictionary representing the adjacency matrix.

    Returns:
        The total cost as an integer.
    """

    total_cost = 0
    visited = set() # Set to keep track of visited edges

    for i in adjacency_matrix:
        for j, cost in adjacency_matrix[i].items():
            edge = tuple(sorted([i, j]))  
            if edge not in visited:  
                total_cost += cost
                visited.add(edge) 
    return total_cost


input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-,
10,-, -, 26, -, 29,-,
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
- ,-,-,21,9,25,-'''

print(maximum_saving(input_network))
