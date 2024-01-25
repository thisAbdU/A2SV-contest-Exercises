class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        i = 0
        while i < len(sorted_s):
            if sorted_t[i] != sorted_s[i]:
                return sorted_t[i]
            i += 1
        
        
        return sorted_t[i]
