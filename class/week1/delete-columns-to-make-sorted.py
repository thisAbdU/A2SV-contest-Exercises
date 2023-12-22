import numpy as np
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        #find the transpose of the strs
        
        listStrs = [list(row) for row in strs]
        transposed = np.transpose(listStrs)  
        
        #compare each row with its reverse
        count = 0
        for row in transposed:
            if "".join(row) != "".join(sorted(row)):
                count += 1
        return count