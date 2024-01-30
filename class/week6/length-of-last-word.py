class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        sList = s.split()
        return len(sList[-1])
        