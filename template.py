class TreeNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TreeNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return curr.is_end

    def startsWith(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return True


