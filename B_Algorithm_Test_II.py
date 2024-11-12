from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_map = {}

    def insert_after(self, new_value, after_value):
        new_node = Node(new_value)
        if after_value in self.node_map:
            after_node = self.node_map[after_value]
            new_node.next = after_node.next
            after_node.next = new_node
            if after_node == self.tail:
                self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head = self.tail = new_node
        self.node_map[new_value] = new_node

    def remove(self, value):
        if value in self.node_map:
            node = self.node_map[value]
            node.value = None  
            
    def to_list(self):
        result = []
        current = self.head
        while current:
            if current.value is not None:
                result.append(current.value)
            current = current.next
        return result

arr = []
for _ in range(int(input())):
    ins = list(input().split())
    arr.append(ins)

linked_list = LinkedList()
dic = defaultdict(int)

for command in arr:
    if command[0] == 'insert':
        a, b = int(command[1]), int(command[2])
        linked_list.insert_after(a, b)
    else:
        va = int(command[1])
        linked_list.remove(va)

res = linked_list.to_list()
print(*res)