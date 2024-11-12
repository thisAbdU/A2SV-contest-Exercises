word_dict = {
    "A": {
        "nodes": 5,
        "edges": 5,
        "connections": [(5, 2), (3, 1), (4, 2), (1, 4), (1, 2)]
    },
    "2": {
        "nodes": 4,
        "edges": 3,
        "connections": [(1, 2), (2, 3), (3, 4)]
    },
    "S": {
        "nodes": 4,
        "edges": 3,
        "connections": [(1, 2), (2, 3), (3, 4)]
    },
    "V": {
        "nodes": 3,
        "edges": 2,
        "connections": [(1, 2), (2, 3)]
    }
}

word = input().strip()
node = word_dict[word]["nodes"]
edge = word_dict[word]["edges"]
connections = word_dict[word]["connections"]

print(node, edge)
for u, v in connections:
    print(u, v)