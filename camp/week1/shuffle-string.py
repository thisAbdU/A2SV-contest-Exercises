class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        toBeshuffled = list(s)
        for i, index in enumerate(indices):
            toBeshuffled[index] = s[i]
        return "".join(toBeshuffled)
            