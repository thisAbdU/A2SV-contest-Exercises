class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        wordIndex = {}

        # Find the common words and store their indices sum
        for index, word in enumerate(list1):
            if word in list2:
                wordIndex[word] = index + list2.index(word)

        # Find the minimum index sum
        minIndexSum = min(wordIndex.values())

        # Filter words with the minimum index sum
        result = [word for word, indexSum in wordIndex.items() if indexSum == minIndexSum]

        return result
