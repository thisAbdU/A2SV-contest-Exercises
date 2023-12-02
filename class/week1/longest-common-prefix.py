from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the word with the minimum length
        def minLength(strs):
            miniLength = float('inf')  # Initialize to a large value
            for i in range(len(strs)):
                if len(strs[i]) < miniLength:
                    miniLength = len(strs[i])
                    minIndex = i
            return minIndex

        minIndex = minLength(strs)
        minWord = strs[minIndex]

        j = 0
        for j in range(len(minWord)):
            # Check if the current character at position j is common to all words
            for i in range(len(strs)):
                if strs[i][j] != minWord[j]:
                    return minWord[:j]

        return minWord[:j+1]

