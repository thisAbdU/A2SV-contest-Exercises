# class TreeNode:
#     def __init__(self):
#         self.is_end = False
#         self.children = [None for i in range(26)]

# class Trie:

#     def __init__(self):
#         self.root = TreeNode()

#     def insert(self, word: str) -> None:
#         curr = self.root

#         for c in word:
#             idx = ord(c) - ord('a')
#             if not curr.children[idx]:
#                 curr.children[idx] = TreeNode()
#             curr = curr.children[idx]
#         curr.is_end = True
#         print(self.count)



# n = int(input())
# dictionary = Trie()
# for t in range(n):
#     word = input()
#     dictionary.insert(word)

    

def collapse(a, b):
    n, m = len(a), len(b)

    if len(a) == 0:
        return m
    
    if len(b) == 0:
        return n
    
    i, j = len(a) - 1, 0
    while a[i] == b[j]:
        i -= 1
        j += 1
        n -= 1
        m -= 1
        if j > len(b) - 1 or i < 0:
            break
    return m + n

def collarpse2(b, a):
    n, m = len(b), len(a)

    if len(b) == 0:
        return m
    
    if len(a) == 0:
        return n
    
    i, j = len(b) - 1, 0
    while b[i] == a[j]:
        i -= 1
        j += 1
        n -= 1
        m -= 1
        if j > len(a) - 1 or i < 0:
            break
    return m + n

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

memo = {}
count = 0

print(count)