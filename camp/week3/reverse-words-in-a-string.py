class Solution:
    def reverseWords(self, s: str) -> str:
        listS = s.split(" ")
        trimmed = []

        for i in range(len(listS) - 1, -1, -1):
            word = listS[i].strip()
            if word:
                trimmed.append(word)

        reversed_string = " ".join(trimmed)
        return reversed_string
