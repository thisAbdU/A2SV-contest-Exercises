from collections import deque


class StringIterator:
    def __init__(self, compressed : str):
        self.uncompressed = deque([])
        for i in range(len(compressed) - 1, 0, -2):
            self.uncompressed.append((compressed[i], compressed[i-1]))

    def next(self) -> chr:
        if self.uncompressed:
            count, character = self.uncompressed.pop()
            if int(count) > 1:
                self.uncompressed.append((int(count) - 1, character))

        return character
        
    def hasNext(self) -> bool:
        if self.uncompressed:
            return True
        return False


word = input()
stringIterator = StringIterator(word)
print(stringIterator.next()) # return "L"
print(stringIterator.next()) # return "e"
print(stringIterator.next()) # return "e"
print(stringIterator.next()) # return "t"
print(stringIterator.next()) # return "C"
print(stringIterator.next()) # return "o"
print(stringIterator.hasNext()) # return True
print(stringIterator.next()) # return "d"
print(stringIterator.hasNext()) # return True

