class Solution:
    def romanToInt(self, s: str) -> int:
        symbolVal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        intValue = 0
        i = 0  # Initialize the loop variable outside the loop

        while i < len(s):
            # Check for special cases (e.g., IV, IX, XL, etc.)
            if i < len(s) - 1 and s[i:i+2] in symbolVal:
                intValue += symbolVal[s[i:i+2]]
                i += 2  # Skip two characters for special cases
            else:
                intValue += symbolVal[s[i]]
                i += 1

        return intValue
