class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigit = ""
        for num in digits:
            newDigit += str(num)
        newDigit = int(newDigit) + 1
        return (list(map(int, str(newDigit))))