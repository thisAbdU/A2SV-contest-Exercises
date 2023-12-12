class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        lastIndex = 0
        for i in spaces:
            output += s[lastIndex:i] + " "
            lastIndex = i
        output += s[i:]
        return output