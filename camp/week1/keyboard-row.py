class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowOne = set("qwertyuiop")
        rowTwo = set("asdfghjkl")
        rowThree = set("zxcvbnm")
        
        output = []
        
        for word in words:
            word_set = set(word.lower())
            
            if word_set.issubset(rowOne) or word_set.issubset(rowTwo) or word_set.issubset(rowThree):
                output.append(word)
                
        return output
