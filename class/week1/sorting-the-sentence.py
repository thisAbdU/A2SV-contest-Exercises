class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        word.sort(key=lambda a:a[-1])
        result = ""
        for characters in word:
            result += characters[:-1] + " "
        return result.strip()