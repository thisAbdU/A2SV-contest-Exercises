class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palid = list(palindrome)
        i = 0
        while i < len(palid)//2:
            if palid[i] != 'a':
                palid[i] = 'a'
                break
            i += 1
        
        if i == len(palid)//2:
            palid[-1] = 'b'
        
        return "".join(palid)