class Solution:
    def longestPalindrome(self, s: str) -> int:
        countLetter = Counter(s)
        len_ = 0
        for letter_freq in countLetter.values():
            len_ += letter_freq - (letter_freq%2)

            len_ += ((len_ % 2 == 0) and ( letter_freq % 2 == 1 ))
            print(letter_freq)
        return len_
       