class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        count = 0
        max_count = 0
        vowels = "aeiou"
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            while right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            max_count = max(max_count, count)
        return max_count
