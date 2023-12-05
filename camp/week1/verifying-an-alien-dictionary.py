class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDic = {values: i for i, values in enumerate(order)}
        
        for i in range(len(words) - 1):
            wordOne, wordTwo = words[i], words[i+1]
            
            for j in range(len(wordOne)):
                if j == len(wordTwo):
                    return False
                
                if wordOne[j] != wordTwo[j]:
                    if orderDic[wordOne[j]] > orderDic[wordTwo[j]]:
                        return False
                    break
                    
        return True
                    