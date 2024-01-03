class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            numList = [int(digit) for digit in str(num)]
            numList.sort()

            i = 0
            while i < len(numList) and numList[0] == 0:
                if numList[i] != 0:
                    numList[0], numList[i] = numList[i], numList[0]
                    break
                i += 1

            numStr = ''.join(map(str, numList))
            return int(numStr)
        elif num < 0:
            numList = [int(digit) for digit in str(num)[1:]]
            
            # Check if there are any digits after the minus sign
            if not numList:
                return 0  # Handle the case of a negative number with no digits

            numList.sort(reverse=True)
            numStr = '-' + ''.join(map(str, numList))
            return int(numStr)
        else:
            return 0  # Handle the case of zero
