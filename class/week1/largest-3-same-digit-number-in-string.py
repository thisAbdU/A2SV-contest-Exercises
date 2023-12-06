class Solution:
    def largestGoodInteger(self, num: str) -> str:
        possibleNum = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        for i in range(len(possibleNum)):
            if possibleNum[i] in num:
                return possibleNum[i]
        return ""