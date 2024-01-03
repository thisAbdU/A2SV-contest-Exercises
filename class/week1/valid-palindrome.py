class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleanS = ""
        for char in s:
            if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                cleanS += char
        return cleanS[::-1] == cleanS
